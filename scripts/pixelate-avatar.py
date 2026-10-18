"""
Transforme la photo de profil en avatar pixel art (PNG natif, fond détouré en disque).

    python3 scripts/pixelate-avatar.py public/me_avatar.jpg public/me_avatar_pixel.png

Dépendance : Pillow (pip install pillow).
La palette est calculée surtout sur le visage (zone centrale) pour garder des
nuances de peau lisibles, le reste des couleurs sert au fond et aux vêtements.
L'image est affichée agrandie sans lissage (classe `pixelated`) et animée en CSS.
"""

import argparse

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

# Zone du visage, en fractions de l'image (cadrage buste centré)
FACE_BOX = (0.27, 0.08, 0.73, 0.74)


def circle_mask(size: int) -> Image.Image:
    big = Image.new("L", (size * 8, size * 8), 0)
    ImageDraw.Draw(big).ellipse((4, 4, size * 8 - 4, size * 8 - 4), fill=255)
    return big.resize((size, size), Image.BOX).point(lambda v: 255 if v > 128 else 0)


def build_palette(img: Image.Image, face_colors: int, other_colors: int) -> Image.Image:
    w, h = img.size
    x0, y0, x1, y1 = FACE_BOX
    face = img.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
    face_pal = face.quantize(colors=face_colors, method=Image.Quantize.MEDIANCUT).getpalette()
    full_pal = img.quantize(colors=other_colors, method=Image.Quantize.MEDIANCUT).getpalette()
    colors = face_pal[: face_colors * 3] + full_pal[: other_colors * 3]
    palette = Image.new("P", (1, 1))
    palette.putpalette(colors + [0] * (768 - len(colors)))
    return palette


def pixelate(src: str, size: int, face_colors: int, other_colors: int) -> Image.Image:
    img = Image.open(src).convert("RGB")
    img = ImageEnhance.Color(img).enhance(1.3)
    img = ImageEnhance.Contrast(img).enhance(1.15)
    img = img.filter(ImageFilter.UnsharpMask(radius=4, percent=180, threshold=2))
    palette = build_palette(img, face_colors, other_colors)
    small = img.resize((size, size), Image.BOX)
    out = small.quantize(palette=palette, dither=Image.Dither.NONE).convert("RGBA")
    out.putalpha(circle_mask(size))
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("src")
    parser.add_argument("dest")
    parser.add_argument("--size", type=int, default=64, help="côté en pixels (défaut 64)")
    parser.add_argument("--face-colors", type=int, default=16)
    parser.add_argument("--other-colors", type=int, default=5)
    args = parser.parse_args()
    pixelate(args.src, args.size, args.face_colors, args.other_colors).save(args.dest, optimize=True)


if __name__ == "__main__":
    main()
