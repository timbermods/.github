# Timbermods sites

All nine were redesigned with this flow on 2026-09-23 and are live. Each repo's CLAUDE.md has the full per-site
detail: design rules, test, preview, publish, and the release-update checklist.

| Repo (timbermods/…) | Site dir | Look | Site test | Publish |
|---|---|---|---|---|
| BeaverBuddies-MultiColony | docs/ | River Station Signage (enamel plates on timber posts; amber = colony 1, teal = colony 2) | none; CLAUDE.md gives `node --check` and a link check | Pages main:/docs |
| BeaverBuddies-Stability-Fork | docs/ | Blued steel and pine; hero is one shared colony with two players' cursors and an In sync panel (dark only) | none; CLAUDE.md gives grep checks | Pages main:/docs |
| MixedStorage | site/ | Walnut apothecary drawer cabinet | `node tests/test-site.mjs` | merge, then `.\deploy-site.ps1` → gh-pages |
| LateGamePerformance | docs/ | Pit Crew (pit board, crew stations, timing tower) | none (no CI; mod tests run locally) | Pages main:/docs |
| OptimizedLocalHousing | docs/ | Banquet-hall seating plan | none (mod CI only) | Pages main:/docs |
| HungryPathing | docs/ (design records in docs/) | Enamel yard signs / works canteen | `node tests/test-site.mjs` | Pages main:/docs |
| PersistentWorkAreas | docs/ | Drafting plan with vellum overlays | none (mod CI only) | Pages main:/docs |
| timberborn-tipsy-tail | docs/ | Poolside bar | `python Source/validate_version.py` | Pages main:/docs |
| timbermods.github.io (hub) | repo root | Lodge wall: walnut boards on birch (day) / forest floor (night); each mod a paper or moss panel in its own colour and art | `node scripts/test-site.mjs` | Pages main:/ (release data refreshed hourly by a bot) |

## Shared across the sites

- **`release.js`:** byte-identical on the Stability Fork, MixedStorage, Late Game Performance, Optimized Local Housing,
  Hungry Pathing and The Tipsy Tail. Replace it, never edit it. MultiColony has its own variant (it fills versions from
  the newest published pre-release). Persistent Work Areas and the hub use their own `site.js`.
- **Mod accents used on the hub:** Stability Fork #b8322a, MultiColony #1a6a77, Late Game Performance #5b3fd0,
  Optimized Local Housing #2d5f9a, Hungry Pathing #1d4a86, MixedStorage #8a6a2c, Persistent Work Areas #8a6512,
  The Tipsy Tail #1a6773.
- **Mod pictures on the hub:** when a site's look changes, recapture its picture with `python scripts/card-art.py <id>`
  in the hub repo.
- **Org profile** (`timbermods/.github`, `profile/`): its README repeats each mod's hub text, accent, category and
  group. Its per-mod pictures are rendered from the live hub by `python profile/make_images.py`; re-run that after a
  hub picture changes. Its banner, `banner.svg`, is a drawn beaver valley at dusk made by `profile/make_banner.py`; never build a banner
  from the mods' pictures. The hub opens on the same valley (`assets/img/make_valley.py`, day and dusk); change both
  together.
- **Kyler's taste (hub and profile):** no "card"/binder wording in visible text; wood, brown and green over black/white;
  no banners composited from mod pictures; every picture must show what the mod actually does.
- **A new site's look must differ from every look above.**
