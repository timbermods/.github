"""Draws the Timbermods organization avatar: a pine growing up through a brass gear (timber and mods), 512x512 SVG.

    python profile/avatar/make_avatar.py      (writes timbermods-avatar.svg next to this script)

Upload a PNG of it (1024x1024) at github.com/organizations/timbermods/settings/profile. It is the org's own art, not a
Timberborn asset."""
import math, os

HERE = os.path.dirname(os.path.abspath(__file__))
f1 = lambda v: f"{v:.1f}".rstrip("0").rstrip(".")

DEFS = """<defs>
  <radialGradient id="bg" cx="50%" cy="38%" r="75%">
    <stop offset="0" stop-color="#2c4a33"/><stop offset=".6" stop-color="#1c3024"/><stop offset="1" stop-color="#121e17"/>
  </radialGradient>
  <radialGradient id="glow" cx="50%" cy="46%" r="50%">
    <stop offset="0" stop-color="#eaa94f" stop-opacity=".3"/><stop offset="1" stop-color="#eaa94f" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="brass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e2bd72"/><stop offset=".5" stop-color="#c19a5b"/><stop offset="1" stop-color="#8a6a2c"/></linearGradient>
</defs>
<rect width="512" height="512" fill="url(#bg)"/>
<rect width="512" height="512" fill="url(#glow)"/>"""


def svg(body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">\n{DEFS}\n{body}\n</svg>\n'



def pine(cx, top, h, w, dark, light):
    out = []
    for t, b, ww in [(top, top + h * .42, w * .5), (top + h * .24, top + h * .7, w * .75), (top + h * .48, top + h * .96, w)]:
        out.append(f'<path d="M{f1(cx)} {f1(t)} L{f1(cx + ww / 2)} {f1(b)} L{f1(cx - ww / 2)} {f1(b)} Z" fill="{dark}"/>')
        out.append(f'<path d="M{f1(cx)} {f1(t)} L{f1(cx)} {f1(b)} L{f1(cx - ww / 2)} {f1(b)} Z" fill="{light}"/>')
    out.append(f'<rect x="{f1(cx - w * .07)}" y="{f1(top + h * .96)}" width="{f1(w * .14)}" height="{f1(h * .14)}" fill="#56402a"/>')
    return "".join(out)




def gear_pine():
    """A pine growing up through the middle of a big brass gear: timber and mods, as a badge."""
    teeth = "".join(f'<rect x="-22" y="-218" width="44" height="46" rx="8" fill="url(#brass)" transform="rotate({a})"/>' for a in range(0, 360, 30))
    bolts = "".join(f'<circle cx="{f1(160 * math.cos(math.radians(a)))}" cy="{f1(160 * math.sin(math.radians(a)))}" r="7" fill="#8a6a2c"/>' for a in range(15, 360, 60))
    return svg(f"""
<g transform="translate(256 262)">
  <circle r="200" fill="#0f1a13" opacity=".45" transform="translate(0 10)"/>
  {teeth}
  <circle r="186" fill="url(#brass)"/>
  <circle r="186" fill="none" stroke="#6e5222" stroke-width="4"/>
  <circle r="150" fill="#1c3024"/>
  <circle r="150" fill="none" stroke="#6e5222" stroke-width="6"/>
  {bolts}
</g>
<!-- the hill and the pine inside the gear's hole -->
<clipPath id="hole"><circle cx="256" cy="262" r="146"/></clipPath>
<g clip-path="url(#hole)">
  <rect x="100" y="110" width="312" height="310" fill="#223b2b"/>
  <circle cx="256" cy="200" r="120" fill="#eaa94f" opacity=".16"/>
  <path d="M100 360 C170 330 342 330 412 360 V420 H100 Z" fill="#2f5d3a"/>
  {pine(256, 118, 228, 176, "#2f5d3a", "#4a8a52")}
  {"".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#f3e3b8" opacity=".8"/>' for x, y in [(160, 170), (340, 150), (180, 250), (350, 230)])}
</g>
<!-- the pine's tip breaks out over the top of the gear -->
<path d="M256 80 L290 150 L222 150 Z" fill="#2f5d3a"/><path d="M256 80 L256 150 L222 150 Z" fill="#4a8a52"/>""")



if __name__ == "__main__":
    with open(os.path.join(HERE, "timbermods-avatar.svg"), "w", encoding="utf-8") as f:
        f.write(gear_pine())
    print("made timbermods-avatar.svg")
