"""Renders the organization profile's picture for each mod: profile/cards/<id>.png (640x400).

Each is that mod's picture from the catalog (timbermods.github.io, which takes it from the mod's own site) in a clear
sleeve on a dark board, framed in the mod's own colour. The pictures are fetched from the live catalog; the board and
sleeve textures and the Anybody font are kept in profile/src/, so the catalog's own look can change without breaking
this. Re-run it after a mod's picture changes in the catalog:

    python profile/make_images.py

Needs Python with playwright, and Microsoft Edge installed (it drives the installed Edge; no browser download).
"""
import base64, os
from playwright.sync_api import sync_playwright

HUB = "https://timbermods.github.io/"
SRC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")


def data_uri(name, mime):
    with open(os.path.join(SRC_DIR, name), "rb") as f:
        return "data:" + mime + ";base64," + base64.b64encode(f.read()).decode()


FONT = data_uri("anybody-latin-700-normal.woff2", "font/woff2")
BOARD = data_uri("binder.webp", "image/webp")
SHEEN = data_uri("sheen.webp", "image/webp")
OUT = os.path.dirname(os.path.abspath(__file__))
# card id, accent, category pill (the catalog's order and wording)
CARDS = [
    ("beaverbuddies-stability-fork", "#b8322a", "Multiplayer"),
    ("timber-together", "#1a6a77", "Multiplayer"),
    ("late-game-performance", "#5b3fd0", "Performance"),
    ("optimized-local-housing", "#2d5f9a", "Housing"),
    ("hungry-pathing", "#1d4a86", "Beaver needs"),
    ("mixedstorage", "#8a6a2c", "Storage"),
    ("persistent-work-areas", "#8a6512", "Planning"),
    ("the-tipsy-tail", "#1a6773", "Building"),
]

BASE = f"""
<style>
@font-face {{ font-family: Anybody; font-weight: 700; src: url("{FONT}") format("woff2"); }}
* {{ box-sizing: border-box; margin: 0; }}
body {{ background: transparent; }}
.page {{ background: #1d1f23 url("{BOARD}"); }}
.sleeve {{ position: relative; padding: 7px; border-radius: 14px; background: rgba(255,255,255,.07);
  border: 1px solid rgba(255,255,255,.16); border-top-color: rgba(255,255,255,.32); box-shadow: 0 8px 18px -8px rgba(0,0,0,.7); }}
.sleeve::after {{ content: ""; position: absolute; inset: 0; border-radius: inherit;
  background: url("{SHEEN}") 95% 0 / 220% 220% no-repeat; opacity: .4; }}
.card {{ position: relative; border: 6px solid var(--c); border-radius: 9px; overflow: hidden; background: var(--c); }}
.card img {{ display: block; width: 100%; height: 100%; object-fit: cover; }}
.pill {{ position: absolute; left: 14px; top: 14px; padding: 6px 13px 7px; border-radius: 999px; background: var(--c); color: #fff;
  font: 700 17px/1 Anybody, sans-serif; letter-spacing: .02em; box-shadow: 0 0 0 2px rgba(255,255,255,.85); }}
</style>"""


def card_html(cid, accent, pill):
    return BASE + f"""
<div id="shot" class="page" style="width:640px;height:400px;padding:14px 16px;border-radius:12px">
  <div class="sleeve" style="height:100%"><div class="card" style="--c:{accent};height:100%">
    <img src="{HUB}assets/img/cards/{cid}.webp" alt="">
  </div></div>
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
    browser.close()
