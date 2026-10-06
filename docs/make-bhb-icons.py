"""Home-screen icons for the BHB Training phone app (assets/brand/bhb-*.png).
Same family as the Staff Portal's icons (sage square, BHB in bone, gold subtitle) so a phone with both can tell
them apart by the subtitle. Needs Pillow. Run from the repo root: python docs/make-bhb-icons.py"""
from PIL import Image, ImageDraw, ImageFont

SAGE = (78, 95, 79, 255); BONE = (247, 247, 247, 255); GOLD = (201, 165, 107, 255)
FONT = "C:/Windows/Fonts/georgiab.ttf"

def mark(d, size, scale):
    bh = ImageFont.truetype(FONT, round(size * 0.27 * scale / 0.78))
    sub_size = round(size * 0.088 * scale / 0.78)
    sub = ImageFont.truetype(FONT, sub_size)
    cx, cy = size / 2, size * 0.5
    bb = d.textbbox((0, 0), "BHB", font=bh); h = bb[3] - bb[1]
    y = cy - h * 0.85
    d.text((cx, y), "BHB", font=bh, fill=BONE, anchor="ma")
    label = "TRAINING"; gap = round(sub_size * 0.3)
    ws = [d.textlength(c, font=sub) for c in label]
    x = cx - (sum(ws) + gap * (len(label) - 1)) / 2
    for c, w in zip(label, ws):
        d.text((x, y + h * 1.28), c, font=sub, fill=GOLD, anchor="la"); x += w + gap

def rounded(size):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=round(size * .1875), fill=SAGE); mark(d, size, .78); return im

def maskable(size):
    im = Image.new("RGBA", (size, size), SAGE); mark(ImageDraw.Draw(im), size, .62); return im

def square(size):  # iOS rounds the corners itself, so it wants a full square
    im = Image.new("RGB", (size, size), SAGE[:3]); mark(ImageDraw.Draw(im), size, .72); return im

def fav(size):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=round(size * .22), fill=SAGE)
    d.text((size / 2, size / 2 + size * .03), "BHB", font=ImageFont.truetype(FONT, round(size * .44)), fill=BONE, anchor="mm"); return im

if __name__ == "__main__":
    o = "assets/brand/"
    rounded(192).save(o + "bhb-192.png"); rounded(512).save(o + "bhb-512.png"); rounded(1024).save(o + "bhb-1024.png")
    maskable(512).save(o + "bhb-maskable-512.png"); fav(64).save(o + "bhb-64.png")
    square(1024).resize((180, 180), Image.LANCZOS).save(o + "bhb-180.png")  # drawn big, then shrunk, so the small lettering stays clean
