"""Original weather icon set (flat, 256x256 SVG + PNG)."""
import math, os
import cairosvg  # pip install cairosvg

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")  # repo root
os.makedirs(f"{OUT}/svg", exist_ok=True)
os.makedirs(f"{OUT}/png", exist_ok=True)

# Palette
SUN, SUN_CORE = "#FFB020", "#FFC94D"
CLOUD_LIGHT, CLOUD_MID, CLOUD_DARK = "#DCE3EA", "#B4C0CC", "#8593A3"
RAIN = "#2F7FE0"
SNOW = "#5AA9E6"
BOLT = "#FFC21A"
FOG = "#A3AFBC"


def sun(cx, cy, r, rays=True):
    s = ""
    if rays:
        for i in range(8):
            a = math.radians(i * 45 + 22.5)
            x1, y1 = cx + math.cos(a) * (r + 12), cy + math.sin(a) * (r + 12)
            x2, y2 = cx + math.cos(a) * (r + 12 + r * 0.42), cy + math.sin(a) * (r + 12 + r * 0.42)
            s += (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                  f'stroke="{SUN}" stroke-width="{max(6, r*0.2):.1f}" stroke-linecap="round"/>')
    s += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SUN}"/>'
    s += f'<circle cx="{cx - r*0.18:.1f}" cy="{cy - r*0.18:.1f}" r="{r*0.62:.1f}" fill="{SUN_CORE}"/>'
    return s


def cloud(cx, base, k=1.0, fill=CLOUD_LIGHT):
    """Cloud whose flat bottom sits at y=base, centred on cx, scale k (width ~170*k)."""
    shapes = [
        ("rect", -85, -48, 170, 48, 24),
        ("circle", -42, -48, 34),
        ("circle", 12, -64, 46),
        ("circle", 56, -40, 28),
    ]
    g = f'<g transform="translate({cx},{base}) scale({k})" fill="{fill}">'
    for sh in shapes:
        if sh[0] == "rect":
            _, x, y, w, h, rx = sh
            g += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/>'
        else:
            _, x, y, r = sh
            g += f'<circle cx="{x}" cy="{y}" r="{r}"/>'
    return g + "</g>"


def drop(x, y, k=1.0):
    return (f'<path transform="translate({x},{y}) scale({k}) rotate(15)" fill="{RAIN}" '
            'd="M0,-16 C6,-6 11,1 11,7 A11,11 0 0 1 -11,7 C-11,1 -6,-6 0,-16Z"/>')


def flake(x, y, k=1.0):
    arms = ""
    for i in range(6):
        a = i * 60
        arms += (f'<g transform="rotate({a})"><line x1="0" y1="0" x2="0" y2="-15"/>'
                 '<polyline points="-5,-12 0,-8 5,-12" fill="none"/></g>')
    return (f'<g transform="translate({x},{y}) scale({k})" stroke="{SNOW}" stroke-width="3.6" '
            f'stroke-linecap="round" stroke-linejoin="round">{arms}'
            f'<circle r="2.6" fill="{SNOW}" stroke="none"/></g>')


def bolt(x, y, k=1.0):
    return (f'<path transform="translate({x},{y}) scale({k})" fill="{BOLT}" stroke="#FFFFFF" '
            'stroke-width="5" stroke-linejoin="round" paint-order="stroke" '
            'd="M6,-40 L-20,4 L-2,4 L-10,40 L20,-8 L2,-8 L12,-40Z"/>')


def fog_lines(rows):
    s = ""
    for (x1, x2, y) in rows:
        s += (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{FOG}" '
              'stroke-width="12" stroke-linecap="round"/>')
    return s


def svg(body):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" '
            f'width="256" height="256">{body}</svg>')


CLOUD_BASE = 150  # standard cloud baseline for precipitation icons

icons = {
    "sunny": sun(128, 128, 54),
    "sunny_s_cloudy": sun(116, 110, 48) + cloud(162, 206, 0.62),
    "partly_cloudy": sun(98, 96, 40) + cloud(140, 196, 0.9),
    "cloudy": cloud(150, 150, 0.72, CLOUD_MID) + cloud(116, 200, 0.95),
    "fog": fog_lines([(52, 204, 78), (36, 176, 110), (80, 220, 142), (44, 196, 174)]),
    "fog_s_snow": fog_lines([(52, 204, 64), (36, 176, 96), (80, 220, 128)])
        + flake(78, 184, 1.0) + flake(128, 206, 1.0) + flake(178, 184, 1.0),
    "rain_light": cloud(128, CLOUD_BASE) + drop(104, 190, 0.85) + drop(152, 204, 0.85),
    "rain": cloud(128, CLOUD_BASE) + drop(84, 188) + drop(128, 200) + drop(172, 188)
        + drop(106, 226) + drop(150, 226),
    "rain_heavy": cloud(128, CLOUD_BASE, 1.0, CLOUD_MID)
        + "".join(drop(x, y, 0.9) for x, y in
                  [(70, 180), (106, 186), (142, 180), (178, 186), (88, 218), (124, 224), (160, 218), (196, 222)]),
    "rain_s_snow": cloud(128, CLOUD_BASE) + drop(84, 190) + drop(126, 196) + drop(104, 228)
        + flake(170, 190, 0.95) + flake(154, 228, 0.95),
    "snow_s_rain": cloud(128, CLOUD_BASE) + flake(86, 190, 0.95) + flake(128, 196, 0.95)
        + flake(106, 230, 0.95) + drop(172, 192) + drop(156, 230),
    "snow_light": cloud(128, CLOUD_BASE) + flake(104, 196, 0.95) + flake(154, 208, 0.95),
    "snow": cloud(128, CLOUD_BASE) + flake(84, 190) + flake(128, 198) + flake(172, 190)
        + flake(106, 230) + flake(150, 230),
    "snow_heavy": cloud(128, CLOUD_BASE, 1.0, CLOUD_MID)
        + "".join(flake(x, y, 0.85) for x, y in
                  [(66, 182), (102, 188), (138, 182), (174, 188), (84, 220), (120, 226), (156, 220), (192, 224)]),
    "sunny_s_rain": sun(110, 96, 42) + cloud(160, 170, 0.62)
        + drop(146, 204, 0.85) + drop(178, 214, 0.85),
    "rain_s_sunny": sun(162, 88, 28) + cloud(116, 160, 0.95)
        + drop(84, 198) + drop(124, 206) + drop(104, 236, 0.9),
    "cloudy_s_snow": cloud(160, 120, 0.7, CLOUD_MID) + cloud(116, 160, 0.9)
        + flake(96, 204, 0.9) + flake(144, 214, 0.9),
    "snow_s_cloudy": cloud(164, 116, 0.6, CLOUD_MID) + cloud(120, 150, 0.95)
        + flake(80, 190, 0.95) + flake(124, 198, 0.95) + flake(168, 190, 0.95)
        + flake(102, 230, 0.95) + flake(146, 230, 0.95),
    "thunderstorms": cloud(128, 140, 1.0, CLOUD_DARK) + drop(78, 186) + drop(92, 224)
        + drop(176, 190) + drop(190, 226) + bolt(134, 184, 1.05),
    "thunderstorms_s_snow": cloud(128, 140, 1.0, CLOUD_DARK) + flake(76, 186, 0.95)
        + flake(92, 226, 0.95) + flake(180, 188, 0.95) + flake(192, 228, 0.95) + bolt(134, 184, 1.05),
    "thunderstorms_light_s_snow": cloud(128, 140, 1.0, CLOUD_MID) + flake(76, 186, 0.95)
        + flake(92, 226, 0.95) + flake(180, 188, 0.95) + flake(192, 228, 0.95) + bolt(134, 184, 1.05),
}

for name, body in icons.items():
    s = svg(body)
    with open(f"{OUT}/svg/{name}.svg", "w") as f:
        f.write(s)
    cairosvg.svg2png(bytestring=s.encode(), write_to=f"{OUT}/png/{name}.png",
                     output_width=256, output_height=256)
print(len(icons), "icons")
