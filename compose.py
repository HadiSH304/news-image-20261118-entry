"""Compose the news front page for make.fun news-image-20261118.

Loads the five generated panel illustrations from assets/, draws the
masthead, date and caption bands with PIL, and saves the final
1024x1024 image as image.jpg next to this file (JPEG, quality 88).
Run: python3 compose.py
"""

import os

from PIL import Image, ImageDraw, ImageFont, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")

W, H = 1024, 1024
NAVY = (13, 20, 32)
CREAM = (245, 235, 210)
RED = (178, 34, 34)
DARK_RED = (122, 14, 14)
NEAR_BLACK = (17, 17, 17)
WHITE = (255, 255, 255)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size):
    return ImageFont.truetype(BOLD, size)


def fit_text(draw, text, fnt, max_width):
    """Prefer a single line, shrinking the font down to 16px; wrap only
    if the caption still does not fit at that size."""
    size = fnt.size
    while size >= 16:
        fnt = ImageFont.truetype(BOLD, size)
        if draw.textlength(text, font=fnt) <= max_width:
            return [text], fnt
        size -= 1
    fnt = ImageFont.truetype(BOLD, 16)
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines, fnt


def draw_centered(draw, cx, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)


def panel(img_path, x, y, w, h):
    img = Image.open(img_path).convert("RGB")
    return ImageOps.fit(img, (w, h), Image.LANCZOS), (x, y)


def main():
    canvas = Image.new("RGB", (W, H), NAVY)
    draw = ImageDraw.Draw(canvas)

    # Masthead
    draw_centered(draw, W // 2, 20, "THE WORLD IN ONE DAY", font(26), CREAM)
    draw_centered(draw, W // 2, 52, "WEDNESDAY 18 NOVEMBER 2026", font(50), CREAM)
    draw.rectangle([20, 112, W - 20, 116], fill=RED)

    # Lead panel: summit photo + dark-red caption band
    lead, pos = panel(
        os.path.join(ASSETS, "media-generation-lead-summit-0-c0087b0a-4813-4355-b330-be4513c1b9db.webp"),
        20, 126, 984, 300,
    )
    canvas.paste(lead, pos)
    draw.rectangle([20, 426, W - 20, 470], fill=DARK_RED)
    draw_centered(
        draw, W // 2, 433,
        "TRUMP, XI & PUTIN \u2014 FIRST THREE-WAY SUMMIT \u00b7 SHENZHEN",
        font(24), WHITE,
    )

    # 2x2 grid of story panels
    stories = [
        ("media-generation-panel-iran-0-2a77c144-d3d9-4862-afc8-a56bd301313e.webp",
         "IRAN STRIKES U.S. BASES IN KUWAIT & BAHRAIN"),
        ("media-generation-panel-kerch-0-f65b430d-49e5-4fbb-81af-b6ef854a2a27.webp",
         "UKRAINE HITS KERCH BRIDGE AGAIN"),
        ("media-generation-panel-nvidia-0-2e1e2b45-2d49-438a-9954-b06da9bb1c05.webp",
         "NVIDIA POSTS RECORD $115.8B QUARTER"),
        ("media-generation-panel-ebola-0-aae9c77f-2d90-4b0a-b0f6-6c04b1cdc79d.webp",
         "EBOLA CASES PASS 11,000 IN CONGO"),
    ]
    xs = [20, 520]
    ys = [484, 752]
    for i, (fname, caption) in enumerate(stories):
        x = xs[i % 2]
        y = ys[i // 2]
        img, pos = panel(os.path.join(ASSETS, fname), x, y, 484, 200)
        canvas.paste(img, pos)
        draw.rectangle([x, y + 200, x + 484, y + 256], fill=NEAR_BLACK)
        lines, fnt = fit_text(draw, caption, font(20), 464)
        total_h = len(lines) * fnt.size + (len(lines) - 1) * 4
        ly = y + 200 + (56 - total_h) // 2
        for line in lines:
            draw_centered(draw, x + 242, ly, line, fnt, WHITE)
            ly += fnt.size + 4

    out = os.path.join(HERE, "image.jpg")
    canvas.save(out, "JPEG", quality=88)
    size = os.path.getsize(out)
    print(f"wrote {out}: {W}x{H}, {size} bytes (limit 1048576)")


if __name__ == "__main__":
    main()
