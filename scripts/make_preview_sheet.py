"""Contact sheet of every icon in png/ (alphabetical, 5 columns, filename under each) -> docs/preview_sheet.png."""
import glob, os
from PIL import Image, ImageDraw, ImageFont  # pip install -r scripts/requirements.txt

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")  # repo root
COLS, ICON, CELL_W, CELL_H = 5, 128, 190, 214


def label_font(size=13):
    for name in ("segoeui.ttf", "DejaVuSans.ttf", "Arial.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default(size)


files = sorted(glob.glob(f"{OUT}/png/*.png"))
rows = -(-len(files) // COLS)
sheet = Image.new("RGB", (COLS * CELL_W, rows * CELL_H), "white")
draw = ImageDraw.Draw(sheet)
font = label_font()
for i, path in enumerate(files):
    x, y = (i % COLS) * CELL_W, (i // COLS) * CELL_H
    img = Image.open(path).convert("RGBA").resize((ICON, ICON), Image.LANCZOS)
    sheet.paste(img, (x + (CELL_W - ICON) // 2, y + 20), img)
    label = os.path.basename(path)
    draw.text((x + (CELL_W - draw.textlength(label, font=font)) / 2, y + ICON + 50), label,
              fill="#222222", font=font)
os.makedirs(f"{OUT}/docs", exist_ok=True)
sheet.save(f"{OUT}/docs/preview_sheet.png")
print(len(files), "icons")
