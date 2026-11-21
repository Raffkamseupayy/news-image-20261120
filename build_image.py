#!/usr/bin/env python3
"""Deterministic news collage for 2026-11-20 (UTC). No network, no randomness.

Builds /output/entry.png (1024x1024) from five hand-set news panels + masthead.
Run:  python3 build_image.py            # writes out/entry.png next to this file
      MAKEFUN_OUTPUT_DIR=/tmp/x python3 build_image.py
"""
import os

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", os.path.join(HERE, "out"))

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
F_BOLD = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")
F_BOOK = os.path.join(FONT_DIR, "DejaVuSans.ttf")
F_MONO = os.path.join(FONT_DIR, "DejaVuSansMono-Bold.ttf")

BG = (12, 14, 22)
PAPER = (244, 240, 230)
RED = (206, 38, 44)
INK = (24, 26, 32)
GREY = (150, 154, 164)
CREAM = (232, 226, 210)

PANELS = [
    # (headline, lines of body, tag, accent color)
    ("BRAZIL: POLICE INDICT BOLSONARO",
     ["Federal Police indict the former president",
      "over an alleged 2022 coup plot; prosecutors",
      "cite drafts of a decree to void the election."],
     "RIO DE JANEIRO", (206, 38, 44)),
    ("HONG KONG: 76TH FATAL FIRE",
     ["Fire tears through Tai Po high-rise estate;",
      "dozens die, hundreds missing as rescue teams",
      "search the burned towers through the night."],
     "TAI PO, HONG KONG", (240, 150, 40)),
    ("JAPAN: TAKAICHI SWORN IN",
     ["Sanae Takaichi takes office as the country's",
      "first female prime minister, leading a new",
      "LDP-led coalition government."],
     "TOKYO", (220, 60, 90)),
    ("UN: FIRST GLOBAL AI RESOLUTION",
     ["General Assembly adopts its first resolution",
      "on AI in warfare, urging safeguards for",
      "autonomous weapons systems."],
     "NEW YORK", (70, 140, 230)),
    ("GTA VI SHATTERS LAUNCH RECORDS",
     ["Rockstar's GTA VI sells millions of copies",
      "on day one, topping launch records worldwide",
      "after a decade-long wait."],
     "GLOBAL", (120, 200, 90)),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_panel(draw, xy, pw, ph, headline, body, tag, accent, serif_head):
    x, y = xy
    draw.rectangle([x, y, x + pw, y + ph], fill=PAPER, outline=(210, 205, 192), width=2)
    draw.rectangle([x, y, x + 7, y + ph], fill=accent)
    tx = x + 22
    tw = pw - 40
    hf = font(F_BOLD, 27)
    yy = y + 18
    for ln in wrap(draw, headline, hf, tw):
        draw.text((tx, yy), ln, font=hf, fill=INK)
        yy += 32
    yy += 4
    bf = font(F_BOOK, 18)
    for ln in body:
        for seg in wrap(draw, ln, bf, tw):
            draw.text((tx, yy), seg, font=bf, fill=(70, 72, 80))
            yy += 23
    tf = font(F_MONO, 15)
    draw.text((tx, y + ph - 30), tag, font=tf, fill=accent)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.text((32, 26), "THE DAILY SIGNAL", font=font(F_BOLD, 52), fill=PAPER)
    d.text((36, 92), "WORLD NEWS  \u00b7  FRIDAY, 20 NOVEMBER 2026", font=font(F_MONO, 24), fill=CREAM)
    d.text((36, 126), "Five stories that shaped the day, in one page.", font=font(F_BOOK, 19), fill=GREY)
    d.line([32, 158, W - 32, 158], fill=RED, width=4)

    # ---- panel grid: 2 columns, 5 stories (3 left, 2 right) ----
    gx, gy, gap = 32, 180, 16
    pw = (W - 2 * 32 - gap) // 2          # 472
    ph = 252
    slots = [(gx, gy), (gx, gy + ph + gap), (gx, gy + 2 * (ph + gap)),
             (gx + pw + gap, gy), (gx + pw + gap, gy + ph + gap)]
    for (x, y), (head, body, tag, accent) in zip(slots, PANELS):
        draw_panel(d, (x, y), pw, ph, head, body, tag, accent, False)

    # ---- footer strip ----
    d.line([32, H - 64, W - 32, H - 64], fill=(60, 62, 74), width=2)
    d.text((32, H - 48), "news-image-20261120  \u00b7  all times UTC  \u00b7  sources: wire reports of 20 Nov 2026",
           font=font(F_MONO, 17), fill=GREY)

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, "entry.png")
    img.save(out_path, "PNG", optimize=True)
    print("wrote", out_path)


if __name__ == "__main__":
    main()
