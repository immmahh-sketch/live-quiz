"""Cartoon logo from the host's photo: cut out, cartoonise, yellow background, purple question mark."""
import sys, os
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from rembg import remove, new_session

SRC = r"C:\Users\GM\.claude\uploads\0986edfa-2db3-420f-bd0f-00a817df85e0\7c7c5bec-image.jpg"
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
YELLOW = (255, 214, 10)
PURPLE = (91, 61, 245)
PURPLE_DARK = (58, 32, 190)

# ---- 1. cut out ----
img = Image.open(SRC).convert("RGB")
img.thumbnail((1400, 1400))
session = new_session("u2net_human_seg")
cut = remove(img, session=session, post_process_mask=True)
alpha = np.array(cut.split()[-1])
ys, xs = np.where(alpha > 20)
x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
pad = 20
cut = cut.crop((max(0, x0 - pad), max(0, y0 - pad), min(cut.width, x1 + pad), min(cut.height, y1 + pad)))

# ---- 2. cartoonise the colour ----
rgb = np.array(cut.convert("RGB"))
a = np.array(cut.split()[-1])
smooth = rgb.copy()
for _ in range(2):
    smooth = cv2.bilateralFilter(smooth, d=9, sigmaColor=60, sigmaSpace=9)
smooth = cv2.edgePreservingFilter(smooth, flags=cv2.RECURS_FILTER, sigma_s=40, sigma_r=0.35)
# quantise to a handful of colours
Z = smooth.reshape((-1, 3)).astype(np.float32)
K = 10
_, labels, centers = cv2.kmeans(Z, K, None, (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0), 3, cv2.KMEANS_PP_CENTERS)
quant = centers[labels.flatten()].reshape(smooth.shape).astype(np.uint8)
# boost saturation a touch
hsv = cv2.cvtColor(quant, cv2.COLOR_RGB2HSV).astype(np.int16)
hsv[..., 1] = np.clip(hsv[..., 1] * 1.25, 0, 255)
quant = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2RGB)
# ink outlines: from the smoothed image so stubble and skin texture do not become grit, then drop specks
gray = cv2.cvtColor(smooth, cv2.COLOR_RGB2GRAY)
gray = cv2.medianBlur(gray, 9)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 19, 6)
ink = (edges < 128).astype(np.uint8)
ink = cv2.morphologyEx(ink, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
n, lab, stats, _ = cv2.connectedComponentsWithStats(ink, connectivity=8)
keep = np.zeros_like(ink)
for i in range(1, n):
    if stats[i, cv2.CC_STAT_AREA] >= 120: keep[lab == i] = 1
ink = cv2.dilate(keep, np.ones((2, 2), np.uint8)).astype(bool)
toon = quant.copy()
toon[ink] = (toon[ink] * 0.25).astype(np.uint8)
# thick outline around the whole silhouette
mask = (a > 20).astype(np.uint8) * 255
mask = cv2.medianBlur(mask, 9)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
outline = cv2.dilate(mask, kernel) - mask
toon_rgba = np.dstack([toon, mask])
toon_img = Image.fromarray(toon_rgba, "RGBA")
outline_img = Image.fromarray(np.dstack([np.zeros_like(toon) + np.array([38, 22, 90], np.uint8), outline]), "RGBA")
subject = Image.alpha_composite(outline_img, toon_img)

def qmark(h, colour=PURPLE, outline=(255, 255, 255), stroke=0):
    font = ImageFont.truetype(r"C:\Windows\Fonts\ariblk.ttf", int(h * 0.92))
    tmp = Image.new("RGBA", (int(h * 0.9), int(h * 1.15)), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    bbox = d.textbbox((0, 0), "?", font=font, stroke_width=stroke)
    w, hh = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tmp = Image.new("RGBA", (w + 2 * stroke + 40, hh + 2 * stroke + 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    d.text((20 + stroke - bbox[0], 20 + stroke - bbox[1]), "?", font=font, fill=colour, stroke_width=stroke, stroke_fill=outline)
    return tmp

def fit(im, h):
    r = h / im.height
    return im.resize((int(im.width * r), h), Image.LANCZOS)

# ---- 3. the logo: 1600 x 900, yellow, subject left of centre, question mark right ----
W, H = 1600, 900
logo = Image.new("RGBA", (W, H), YELLOW + (255,))
s = fit(subject, int(H * 0.98))
logo.alpha_composite(s, (int(W * 0.28) - s.width // 2, H - s.height))
q = qmark(int(H * 0.82), PURPLE, (255, 255, 255), stroke=18)
shadow = qmark(int(H * 0.82), PURPLE_DARK, PURPLE_DARK, stroke=18)
qx, qy = int(W * 0.66) - q.width // 2, int(H * 0.08)
logo.alpha_composite(shadow, (qx + 14, qy + 14))
logo.alpha_composite(q, (qx, qy))
logo.convert("RGB").save(os.path.join(OUT, "logo.png"), optimize=True)

# ---- 4. square icon: 1024, face close-up with the question mark overlapping ----
S = 1024
icon = Image.new("RGBA", (S, S), YELLOW + (255,))
# head + hand only: the top ~70% of the subject
head = subject.crop((0, 0, subject.width, int(subject.height * 0.72)))
hs = fit(head, int(S * 1.05))
icon.alpha_composite(hs, (int(S * 0.36) - hs.width // 2, S - hs.height + int(S * 0.02)))
q2 = qmark(int(S * 0.62), PURPLE, (255, 255, 255), stroke=22)
sh2 = qmark(int(S * 0.62), PURPLE_DARK, PURPLE_DARK, stroke=22)
qx2, qy2 = int(S * 0.72) - q2.width // 2, int(S * 0.06)
icon.alpha_composite(sh2, (qx2 + 12, qy2 + 12))
icon.alpha_composite(q2, (qx2, qy2))
icon = icon.convert("RGB")
for size in (1024, 512, 192, 180, 64, 32):
    icon.resize((size, size), Image.LANCZOS).save(os.path.join(OUT, f"icon-{size}.png"), optimize=True)
# maskable icon: same but with safe padding (content within the centre 80%)
mask = Image.new("RGB", (S, S), YELLOW)
inner = icon.resize((int(S * 0.8), int(S * 0.8)), Image.LANCZOS)
mask.paste(inner, ((S - inner.width) // 2, (S - inner.height) // 2))
mask.resize((512, 512), Image.LANCZOS).save(os.path.join(OUT, "icon-maskable-512.png"), optimize=True)
# wide wordmark-less banner for the topbar: subject head + "?" small
banner = Image.new("RGBA", (400, 160), (0, 0, 0, 0))
hb = fit(head, 160)
banner.alpha_composite(hb, (0, 0))
qb = qmark(120, PURPLE, (255, 255, 255), stroke=6)
banner.alpha_composite(qb, (hb.width - 10, 10))
banner = banner.crop(banner.getbbox())
banner.save(os.path.join(OUT, "mark.png"), optimize=True)
print("done", subject.size, logo.size)
