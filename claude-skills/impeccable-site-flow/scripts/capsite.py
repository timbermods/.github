"""Full-page review captures for a site: capsite.py <base-url> <out-dir> [page ...]
Writes desktop.png / desktop-dark.png / mobile.png / mobile-dark.png for the first page (the home page) and
<page>-desktop.png for the others, plus top crops (first 1600 px) of each home capture as *-top.png for viewing."""
import sys, os
from playwright.sync_api import sync_playwright
from PIL import Image
base, out = sys.argv[1].rstrip("/") + "/", sys.argv[2]
pages = sys.argv[3:] or [""]
os.makedirs(out, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")
    shots = [("desktop", 1440, 900, False, "light"), ("desktop-dark", 1440, 900, False, "dark"),
             ("mobile", 390, 844, True, "light"), ("mobile-dark", 390, 844, True, "dark")]
    for name, w, h, mob, scheme in shots:
        ctx = b.new_context(viewport={"width": w, "height": h}, is_mobile=mob, has_touch=mob, color_scheme=scheme, reduced_motion="reduce")
        pg = ctx.new_page(); pg.goto(base + pages[0], wait_until="networkidle")
        # load every image first (lazy ones included), so the capture shows what a scrolling reader sees
        pg.evaluate("document.querySelectorAll('img').forEach(i => i.loading = 'eager')")
        pg.evaluate("async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { scrollTo(0, y); await new Promise(r => setTimeout(r, 40)); } scrollTo(0, 0); }")
        pg.wait_for_function("[...document.images].every(i => i.complete && i.naturalWidth > 0)", timeout=15000)
        pg.wait_for_timeout(300)
        over = pg.evaluate("document.documentElement.scrollWidth - innerWidth")
        path = os.path.join(out, name + ".png"); pg.screenshot(path=path, full_page=True); ctx.close()
        im = Image.open(path); print(name, im.size, "overflow", over)
        im.crop((0, 0, im.size[0], min(im.size[1], 1600 if w > 500 else 2400))).save(os.path.join(out, name + "-top.png"))
    for pgname in pages[1:]:
        ctx = b.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="reduce")
        pg = ctx.new_page(); pg.goto(base + pgname, wait_until="networkidle"); pg.wait_for_timeout(300)
        pg.screenshot(path=os.path.join(out, pgname.replace(".html", "") + "-desktop.png"), full_page=False); ctx.close()
    b.close()
