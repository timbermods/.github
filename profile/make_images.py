"""Renders the organization profile's images in the catalog's look (the collector's binder at timbermods.github.io):
profile/banner.png (1280x360) and profile/cards/<card-id>.png (640x400).

Each card is that mod's catalog card art in a clear sleeve on a binder page, framed in the mod's own colour, so the
profile, the catalog and each mod's own site read as one set. Everything is fetched from the live catalog (its card
art, Anybody font and felt and binder textures), so re-run this after a card's art changes in the catalog:

    python profile/make_images.py

Needs Python with playwright, and Microsoft Edge installed (it drives the installed Edge; no browser download).
"""
import os
from playwright.sync_api import sync_playwright

HUB = "https://timbermods.github.io/"
OUT = os.path.dirname(os.path.abspath(__file__))
# card id, accent, category pill (the catalog's order and wording)
CARDS = [
    ("beaverbuddies-stability-fork", "#b8322a", "Multiplayer"),
    ("beaverbuddies-multicolony", "#1a6a77", "Multiplayer"),
    ("late-game-performance", "#5b3fd0", "Performance"),
    ("optimized-local-housing", "#2d5f9a", "Housing"),
    ("hungry-pathing", "#1d4a86", "Beaver needs"),
    ("mixedstorage", "#8a6a2c", "Storage"),
    ("persistent-work-areas", "#8a6512", "Planning"),
    ("the-tipsy-tail", "#1a6773", "Building"),
]

BASE = f"""
<style>
@font-face {{ font-family: Anybody; font-weight: 800; src: url("{HUB}assets/fonts/anybody-latin-800-normal.woff2") format("woff2"); }}
@font-face {{ font-family: Anybody; font-weight: 700; src: url("{HUB}assets/fonts/anybody-latin-700-normal.woff2") format("woff2"); }}
* {{ box-sizing: border-box; margin: 0; }}
body {{ background: transparent; }}
.page {{ background: #1d1f23 url("{HUB}assets/img/binder.webp"); }}
.sleeve {{ position: relative; padding: 7px; border-radius: 14px; background: rgba(255,255,255,.07);
  border: 1px solid rgba(255,255,255,.16); border-top-color: rgba(255,255,255,.32); box-shadow: 0 8px 18px -8px rgba(0,0,0,.7); }}
.sleeve::after {{ content: ""; position: absolute; inset: 0; border-radius: inherit;
  background: url("{HUB}assets/img/sheen.webp") 95% 0 / 220% 220% no-repeat; opacity: .4; }}
.card {{ position: relative; border: 6px solid var(--c); border-radius: 9px; overflow: hidden; background: var(--c); }}
.card img {{ display: block; width: 100%; height: 100%; object-fit: cover; }}
.pill {{ position: absolute; left: 14px; top: 14px; padding: 6px 13px 7px; border-radius: 999px; background: var(--c); color: #fff;
  font: 700 17px/1 Anybody, sans-serif; letter-spacing: .02em; box-shadow: 0 0 0 2px rgba(255,255,255,.85); }}
</style>"""


def card_html(cid, accent, pill):
    return BASE + f"""
<div id="shot" class="page" style="width:640px;height:400px;padding:14px 16px;border-radius:12px">
  <div class="sleeve" style="height:100%"><div class="card" style="--c:{accent};height:100%">
    <img src="{HUB}assets/img/cards/{cid}.webp" alt=""><span class="pill">{pill}</span>
  </div></div>
</div>"""


def banner_html():
    fan = ""
    n = len(CARDS)
    for i, (cid, accent, _) in enumerate(CARDS):
        angle = -17 + i * 34 / (n - 1)
        x = 22 + i * 44
        y = 96 + abs(i - (n - 1) / 2) * 7
        fan += (f'<div class="sleeve" style="position:absolute;left:{x}px;top:{y}px;width:232px;height:152px;'
                f'transform:rotate({angle}deg);transform-origin:50% 120%;padding:5px;border-radius:11px">'
                f'<div class="card" style="--c:{accent};height:100%;border-width:5px;border-radius:7px">'
                f'<img src="{HUB}assets/img/cards/{cid}.webp" alt=""></div></div>')
    return BASE + f"""
<div id="shot" style="position:relative;width:1280px;height:360px;overflow:hidden;border-radius:14px;
  background:#dcd8cf url('{HUB}assets/img/felt-light.webp')">
  <div style="position:absolute;left:64px;top:92px;color:#1f2124">
    <div style="font:800 84px/.9 Anybody,sans-serif;letter-spacing:-.03em">Timbermods</div>
    <div style="margin-top:22px;font:400 26px/1.3 system-ui,'Segoe UI',sans-serif;color:#3c4046">Mods for Timberborn, a card each.</div>
    <div style="margin-top:8px;font:600 22px/1.3 system-ui,'Segoe UI',sans-serif;color:#4c5056">timbermods.github.io</div>
  </div>
  <div class="page" style="position:absolute;left:696px;top:0;width:600px;height:360px;border-radius:14px 0 0 14px">{fan}</div>
</div>"""


def render(page, html, path, w, h):
    page.set_viewport_size({"width": w, "height": h})
    page.set_content(html, wait_until="networkidle")
    page.evaluate("document.fonts.ready")
    page.wait_for_timeout(300)
    page.locator("#shot").screenshot(path=path, omit_background=True)
    print("made", os.path.relpath(path, OUT))


with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge")
    page = browser.new_page(device_scale_factor=1)
    os.makedirs(os.path.join(OUT, "cards"), exist_ok=True)
    for cid, accent, pill in CARDS:
        render(page, card_html(cid, accent, pill), os.path.join(OUT, "cards", cid + ".png"), 640, 400)
    render(page, banner_html(), os.path.join(OUT, "banner.png"), 1280, 360)
    browser.close()
