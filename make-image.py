#!/usr/bin/env python3
"""Generate the 24 November 2026 front page: 1024x1024 PNG, programmatic text
(Pillow + DejaVu) so every word is spelled correctly and legible.

Layout: black masthead band, one lead story, 6 stories in a 2x3 grid, footer
strip with short one-liners. Run: python3 make-image.py  -> writes entry.png
"""
import sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 246, 236)
INK = (20, 20, 20)
GREY = (90, 90, 90)
RULE = (180, 175, 160)
GOLD = (201, 162, 39)
NAVY = (20, 33, 61)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = FONT_DIR + "DejaVuSerif-Bold.ttf"
SERIF = FONT_DIR + "DejaVuSerif.ttf"
SANS = FONT_DIR + "DejaVuSans.ttf"
SANS_B = FONT_DIR + "DejaVuSans-Bold.ttf"

DATE_LINE = "TUESDAY  24  NOVEMBER  2026"

LEAD = {
    "tag": "TECHNOLOGY",
    "tag_bg": (29, 78, 137),
    "headline": "HUANG RETURNS — $34 BILLION RICHER",
    "summary": ("Jensen Huang reinstated as Nvidia CEO after Trump intervened; "
                "his fortune jumps about $34 billion to $143.8 billion."),
}

GRID = [
    {"tag": "US", "tag_bg": (21, 101, 192),
     "headline": "Trump halts Iowa explosives detonation",
     "summary": "President pauses the planned blast pending a court ruling after the Army invoked emergency powers."},
    {"tag": "ASIA", "tag_bg": (0, 121, 107),
     "headline": "North Korean jet breaches South's airspace",
     "summary": "Seoul orders Ulleung island residents to shelters; jets also scrambled as Russian warplanes enter the zone."},
    {"tag": "UKRAINE WAR", "tag_bg": (156, 27, 27),
     "headline": "Russian death toll in Ukraine nears 500,000",
     "summary": "Leaked records put the toll at about half a million; Moscow warns Estonia of 'open war'."},
    {"tag": "CLIMATE", "tag_bg": (46, 125, 50),
     "headline": "COP31 failure still reverberates",
     "summary": "China calls the summit's collapse disappointing as the fossil-fuel fight drags on."},
    {"tag": "MIDDLE EAST", "tag_bg": (121, 85, 0),
     "headline": "Three tankers ablaze in Strait of Hormuz",
     "summary": "Ships hit by sea mines catch fire as the Iran–US standoff intensifies."},
    {"tag": "TECH", "tag_bg": (29, 78, 137),
     "headline": "States sue Musk firms over Grok images",
     "summary": "US states say the AI chatbot generated sexualised images of people."},
]

FOOTER_ITEMS = [
    "2031 Women's World Cup hosts set",
    "4.1 quake strikes Pakistan",
    "UN warns wars hit food aid for 7.3m",
    "Honda recalls 810,000 vehicles",
]


def wrap(draw, text, font, max_w):
    """Greedy word wrap; returns list of lines."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_chip(draw, x, y, text, bg, font):
    tw = draw.textlength(text, font=font)
    pad_x, pad_y = 10, 5
    w, h = int(tw) + 2 * pad_x, font.size + 2 * pad_y
    draw.rounded_rectangle([x, y, x + w, y + h], radius=4, fill=bg)
    draw.text((x + pad_x, y + pad_y - 1), text, font=font, fill=(255, 255, 255))
    return w, h


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    d.rectangle([0, 0, W, 116], fill=(0, 0, 0))
    f_title = ImageFont.truetype(SERIF_B, 56)
    title = "THE WORLD IN ONE PAGE"
    d.text(((W - d.textlength(title, font=f_title)) / 2, 24), title,
           font=f_title, fill=(255, 255, 255))
    f_date = ImageFont.truetype(SANS, 22)
    d.text(((W - d.textlength(DATE_LINE, font=f_date)) / 2, 84), DATE_LINE,
           font=f_date, fill=(216, 201, 138))
    d.rectangle([0, 116, W, 120], fill=GOLD)

    # --- lead story ---
    x0, y = 36, 140
    f_tag = ImageFont.truetype(SANS_B, 17)
    draw_chip(d, x0, y, LEAD["tag"], LEAD["tag_bg"], f_tag)
    y += 40
    f_head = ImageFont.truetype(SERIF_B, 44)
    lines = wrap(d, LEAD["headline"], f_head, W - 72)
    assert len(lines) <= 2, f"lead headline too long: {lines}"
    for ln in lines:
        d.text((x0, y), ln, font=f_head, fill=INK)
        y += 56
    y += 8
    f_sum = ImageFont.truetype(SANS, 23)
    slines = wrap(d, LEAD["summary"], f_sum, W - 72)
    assert len(slines) <= 2, f"lead summary too long: {slines}"
    for ln in slines:
        d.text((x0, y), ln, font=f_sum, fill=(51, 51, 51))
        y += 32
    d.line([(36, 366), (W - 36, 366)], fill=RULE, width=2)

    # --- 2x3 grid ---
    col_w = (W - 72 - 28) // 2
    row_h = 178
    grid_top = 384
    f_ghead = ImageFont.truetype(SANS_B, 25)
    f_gsum = ImageFont.truetype(SANS, 19)
    f_gtag = ImageFont.truetype(SANS_B, 15)
    for i, story in enumerate(GRID):
        row, col = divmod(i, 2)
        cx = 36 + col * (col_w + 28)
        cy = grid_top + row * row_h
        draw_chip(d, cx, cy, story["tag"], story["tag_bg"], f_gtag)
        hy = cy + 32
        hlines = wrap(d, story["headline"], f_ghead, col_w)
        assert len(hlines) <= 2, f"grid headline too long: {hlines}"
        for ln in hlines:
            d.text((cx, hy), ln, font=f_ghead, fill=INK)
            hy += 31
        hy += 4
        slines = wrap(d, story["summary"], f_gsum, col_w)
        assert len(slines) <= 3, f"grid summary too long: {slines}"
        for ln in slines:
            d.text((cx, hy), ln, font=f_gsum, fill=(51, 51, 51))
            hy += 25
        # column divider
        if col == 0:
            d.line([(512, cy + 4), (512, cy + row_h - 14)], fill=RULE, width=1)
        # row divider
        if row < 2:
            d.line([(36, cy + row_h - 6), (W - 36, cy + row_h - 6)], fill=RULE, width=1)

    # --- footer strip ---
    d.rectangle([0, 930, W, H], fill=NAVY)
    f_foot_b = ImageFont.truetype(SANS_B, 20)
    f_foot = ImageFont.truetype(SANS, 20)
    label = "ALSO TODAY:  "
    items = "  •  ".join(FOOTER_ITEMS)
    label_w = d.textlength(label, font=f_foot_b)
    ilines = wrap(d, items, f_foot, W - 72 - int(label_w))
    assert len(ilines) <= 2, f"footer too long: {ilines}"
    fy = 942
    d.text((36, fy), label, font=f_foot_b, fill=(216, 201, 138))
    d.text((36 + label_w, fy), ilines[0], font=f_foot, fill=(235, 235, 235))
    if len(ilines) > 1:
        d.text((36, fy + 27), ilines[1], font=f_foot, fill=(235, 235, 235))

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
