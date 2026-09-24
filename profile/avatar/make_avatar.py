"""Draws the Timbermods organization avatar: the Timbermods mark (a pine on a cut log end, as in the banner, the
catalog's header and its favicon), centred on the banner's forest-green night. 512x512 SVG.

    python profile/avatar/make_avatar.py      (writes timbermods-avatar.svg next to this script)

Upload a PNG of it (1024x1024) at github.com/organizations/timbermods/settings/profile. It is the org's own art, not a
Timberborn asset. The mark's shapes are the same as in profile/make_banner.py and the catalog's favicon.svg; change them
together.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# the mark, on its own 32-unit grid (as in the banner and the catalog's favicon)
MARK = """<circle cx="16" cy="16" r="14.5" fill="#56402a"/><circle cx="16" cy="16" r="11.5" fill="#e0c79a"/>
<circle cx="16" cy="16" r="8" fill="none" stroke="#c7a878" stroke-width="1.2"/><circle cx="16" cy="16" r="4.5" fill="none" stroke="#c7a878" stroke-width="1.2"/>
<path d="M16 5.5 L22.5 15 H19 L24 22.5 H8 L13 15 H9.5 Z" fill="#2f5d3a"/><rect x="14.6" y="22.5" width="2.8" height="4" fill="#56402a"/>"""

SCALE = 13          # the mark at 13 x 32 = 416 px, centred with a margin of 48 px
OFFSET = (512 - 32 * SCALE) / 2

SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
<defs>
  <radialGradient id="bg" cx="50%" cy="42%" r="75%">
    <stop offset="0" stop-color="#1f3627"/><stop offset=".6" stop-color="#16281e"/><stop offset="1" stop-color="#0d1a14"/>
  </radialGradient>
  <radialGradient id="glow" cx="50%" cy="50%" r="50%">
    <stop offset="0" stop-color="#eaa94f" stop-opacity=".22"/><stop offset="1" stop-color="#eaa94f" stop-opacity="0"/>
  </radialGradient>
</defs>
<rect width="512" height="512" fill="url(#bg)"/>
<rect width="512" height="512" fill="url(#glow)"/>
<circle cx="256" cy="264" r="{16 * SCALE * .92}" fill="#070d0a" opacity=".35"/>
<g transform="translate({OFFSET} {OFFSET}) scale({SCALE})">
{MARK}
</g>
</svg>
"""

if __name__ == "__main__":
    with open(os.path.join(HERE, "timbermods-avatar.svg"), "w", encoding="utf-8") as f:
        f.write(SVG)
    print("made timbermods-avatar.svg")
