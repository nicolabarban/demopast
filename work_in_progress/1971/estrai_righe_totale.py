"""Individua le righe TOTALE PROVINCIA nelle Tav. 3 1971 e ne ritaglia le strisce.

Layout Tav. 3: il fascicolo alterna pagine "basse" (dispari: classi Meno di 5 -> 50-54)
e pagine "alte" (pari: 55-59 -> 75 e piu + Totale + classi particolari da ignorare).
Le tre sezioni (A-Totale, B-Maschi, C-Femmine) scorrono in quest'ordine: nelle province
piccole stanno impilate sulla stessa coppia di pagine, in quelle grandi occupano piu
coppie. La riga di totale di ogni sezione e' l'ultima della sezione, riconoscibile dal
gap verticale ampio che la segue.

Uso:
    python estrai_righe_totale.py <provincia.pdf> <outdir>

Stampa il layout rilevato e scrive le strisce PNG (M/F, pagina bassa L+R, pagina alta L)
pronte per la lettura visiva.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image

DPI = 300
DARK_THRESHOLD = 120
MIN_ROW_DARK = 40      # stampe sottili (es. Trapani) hanno righe poco dense
ROW_MERGE_GAP = 8
SECTION_GAP = 150
MIN_GROUP_HEIGHT = 10  # scarta i filetti sottili di intestazione (h ~ 3-4)
MIN_CLUSTER_ROWS = 4   # un cluster-dati ha molti comuni; l'intestazione poche righe
STRIP_SCALE = 2.0
STRIP_PAD_ABOVE = 8
STRIP_PAD_BELOW = 14


def render(pdf: Path, outdir: Path, prefix: str) -> list[Path]:
    """Render every page of `pdf` to PNG at DPI. Returns the page images in order."""
    subprocess.run(
        ["pdftoppm", "-r", str(DPI), "-png", str(pdf), str(outdir / prefix)],
        check=True,
    )
    return sorted(outdir.glob(f"{prefix}-*.png"), key=lambda p: int(p.stem.split("-")[-1]))


def row_groups(img: Path) -> tuple[int, int, list[tuple[int, int]]]:
    """Return (width, height, text-row groups) for a page image."""
    im = Image.open(img)
    w, h = im.size
    dark = (np.asarray(im.convert("L")) < DARK_THRESHOLD).sum(axis=1)
    rows = [y for y in range(h) if dark[y] > MIN_ROW_DARK]
    groups: list[tuple[int, int]] = []
    start = prev = None
    for y in rows:
        if start is None:
            start = prev = y
        elif y - prev <= ROW_MERGE_GAP:
            prev = y
        else:
            groups.append((start, prev))
            start = prev = y
    if start is not None:
        groups.append((start, prev))
    return w, h, groups


def total_rows(img: Path) -> list[tuple[int, int]]:
    """Rows followed by a wide blank gap -> end of a section -> TOTALE PROVINCIA."""
    _, h, groups = row_groups(img)
    out = []
    for i, g in enumerate(groups):
        nxt = groups[i + 1][0] if i + 1 < len(groups) else h
        if nxt - g[1] > SECTION_GAP and g[1] - g[0] >= MIN_GROUP_HEIGHT:
            out.append(g)
    return out


def sections(pages: list[Path]):
    """Localizza le righe di totale di A, B, C come (pagina_bassa, y), (pagina_alta, y).

    Due layout possibili:
    - a blocchi (n pagine multiplo di 3): ogni sezione occupa n/3 pagine consecutive e
      il totale sta sull'ultima coppia del blocco;
    - impilato (province piccole, 2 o 4 pagine): le tre sezioni stanno sulla stessa
      coppia di pagine, riconosciute dai tre gap di fine sezione.
    """
    n = len(pages)
    if n % 3 == 0 and n >= 6:
        size = n // 3
        lows, highs = [], []
        for idx in range(3):
            block = pages[idx * size : (idx + 1) * size]
            low_page, high_page = block[-2], block[-1]
            # Se la pagina e' piena il totale non ha un gap ampio dopo di se':
            # in quel caso e' semplicemente l'ultima riga della pagina.
            low_hits = total_rows(low_page) or row_groups(low_page)[2][-1:]
            high_hits = total_rows(high_page) or row_groups(high_page)[2][-1:]
            if not low_hits or not high_hits:
                return None, None
            lows.append((low_page, low_hits[-1]))
            highs.append((high_page, high_hits[-1]))
        return lows, highs

    # layout impilato: i tre totali sono gli ultimi tre candidati di ciascun lato
    low_hits = [(p, t) for p in pages[0::2] for t in total_rows(p)]
    high_hits = [(p, t) for p in pages[1::2] for t in total_rows(p)]
    if len(low_hits) < 3 or len(high_hits) < 3:
        return None, None
    return low_hits[-3:], high_hits[-3:]


def strip(img: Path, y0: int, y1: int, dst: Path, half: str) -> None:
    """Crop a total-row band, upscale, and keep the requested half (L/R)."""
    im = Image.open(img)
    w, _ = im.size
    crop = im.crop((0, y0, w, y1))
    crop = crop.resize((int(w * STRIP_SCALE), int((y1 - y0) * STRIP_SCALE)), Image.LANCZOS)
    cw, ch = crop.size
    if half == "L":
        crop = crop.crop((0, 0, cw // 2, ch))
    elif half == "R":
        crop = crop.crop((cw // 2, 0, cw, ch))
    crop.save(dst)


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    pdf, outdir = Path(sys.argv[1]), Path(sys.argv[2])
    outdir.mkdir(parents=True, exist_ok=True)
    prefix = pdf.stem.replace(" ", "")
    pages = render(pdf, outdir, prefix)
    print(f"{pdf.name}: {len(pages)} pagine")

    lows, highs = sections(pages)
    if lows is None:
        print("  !! layout non riconosciuto - verificare a mano")
        return
    for i, tag in enumerate("ABC"):
        print(f"    {tag}: bassa {lows[i][0].name} y={lows[i][1]} | alta {highs[i][0].name} y={highs[i][1]}")

    # indice 1 = B-Maschi, indice 2 = C-Femmine (indice 0 = A-Totale, solo checksum)
    for sex, idx in (("M", 1), ("F", 2)):
        lp, (ly0, ly1) = lows[idx]
        hp, (hy0, hy1) = highs[idx]
        strip(lp, ly0 - STRIP_PAD_ABOVE, ly1 + STRIP_PAD_BELOW, outdir / f"{prefix}_{sex}_lowL.png", "L")
        strip(lp, ly0 - STRIP_PAD_ABOVE, ly1 + STRIP_PAD_BELOW, outdir / f"{prefix}_{sex}_lowR.png", "R")
        strip(hp, hy0 - STRIP_PAD_ABOVE, hy1 + STRIP_PAD_BELOW, outdir / f"{prefix}_{sex}_highL.png", "L")
    print(f"  strisce scritte in {outdir}/{prefix}_*.png")


if __name__ == "__main__":
    main()
