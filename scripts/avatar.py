"""
Génère les avatars du CV à partir de la photo source (disque sur fond blanc) :

- me_avatar.webp       : la photo détourée, seul le disque est conservé
                         (extérieur transparent) — thème classique ;
- me_avatar_pixel.png  : version pixel art 64 px, même détourage — thème rétro.

    python3 scripts/avatar.py assets/me_avatar.jpg public/

Dépendance : Pillow (pip install pillow).
Le disque est inscrit dans l'image carrée ; on le resserre de quelques pixels
pour éliminer le liseré blanc anti-crénelé de la source.
Pour le pixel art, la palette est calculée surtout sur le visage (zone
centrale) pour garder des nuances de peau lisibles ; l'image est affichée
agrandie sans lissage (classe `pixelated`) et animée en CSS.
"""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageStat

# Zone du visage, en fractions de l'image (cadrage buste centré)
FACE_BOX = (0.27, 0.08, 0.73, 0.74)
# Retrait du bord du disque (en fraction du rayon) pour ôter le liseré blanc
EDGE_INSET = 0.008
SUPERSAMPLE = 8


def disc_mask(size: int, inset: float = EDGE_INSET) -> Image.Image:
    """Disque inscrit, anti-crénelé (sur-échantillonné puis réduit)."""
    big = size * SUPERSAMPLE
    margin = big * inset / 2 + SUPERSAMPLE / 2
    mask = Image.new("L", (big, big), 0)
    ImageDraw.Draw(mask).ellipse((margin, margin, big - margin, big - margin), fill=255)
    return mask.resize((size, size), Image.LANCZOS)


def cutout(src: Image.Image) -> Image.Image:
    out = src.convert("RGBA")
    out.putalpha(disc_mask(src.width))
    return out


def fill_outside(img: Image.Image) -> Image.Image:
    """Prolonge les couleurs du bord du disque vers l'extérieur, pour que les
    filtres (netteté, réduction) ne mélangent pas le fond au contour."""
    spread = img.convert("RGBa").filter(ImageFilter.GaussianBlur(12)).convert("RGBA")
    mean = tuple(int(v) for v in ImageStat.Stat(img.convert("RGB"), mask=img.getchannel("A")).mean)
    base = Image.alpha_composite(Image.new("RGBA", img.size, mean + (255,)), spread)
    return Image.alpha_composite(base, img).convert("RGB")


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


def pixelate(photo: Image.Image, size: int, face_colors: int, other_colors: int) -> Image.Image:
    img = fill_outside(photo)
    img = ImageEnhance.Color(img).enhance(1.3)
    img = ImageEnhance.Contrast(img).enhance(1.15)
    img = img.filter(ImageFilter.UnsharpMask(radius=4, percent=180, threshold=2))
    palette = build_palette(img, face_colors, other_colors)
    small = img.resize((size, size), Image.BOX)
    out = small.quantize(palette=palette, dither=Image.Dither.NONE).convert("RGBA")
    # Pixels entièrement dans le disque ou presque : pas de demi-pixels en bordure
    out.putalpha(disc_mask(size, inset=0).point(lambda v: 255 if v > 128 else 0))
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("src", help="photo source carrée (disque sur fond blanc)")
    parser.add_argument("dest", help="dossier de sortie (public/)")
    parser.add_argument("--size", type=int, default=64, help="côté de l'avatar pixel (défaut 64)")
    parser.add_argument("--face-colors", type=int, default=16)
    parser.add_argument("--other-colors", type=int, default=5)
    args = parser.parse_args()

    dest = Path(args.dest)
    photo = cutout(Image.open(args.src).convert("RGB"))
    photo.save(dest / "me_avatar.webp", quality=88, method=6)
    pixelate(photo, args.size, args.face_colors, args.other_colors).save(dest / "me_avatar_pixel.png", optimize=True)


if __name__ == "__main__":
    main()
