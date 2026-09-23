# CLAUDE.md template (website section)

Fill every `<…>` from the repo's PRODUCT.md, DESIGN.md, `.impeccable/`, README and CI. Keep it standalone: a session
with no memory and no personal skills must be able to update the site correctly from this file alone. Use exact
commands and paths, and keep the prose short. If the repo already has a CLAUDE.md, add or replace the "Website"
section and leave the rest alone.

---

# CLAUDE.md

<One or two lines: what this repo is (the mod), what it builds on, where the source and tests live, and how changes
land on main (PR → merge).>

## Standing rules

- Never launch or drive Timberborn, and never touch installed mods or saves. The maintainer (Kyler) playtests himself.
- Commit on a branch and open a PR. Merge only when Kyler says so in the chat.
- <Anything repo-specific: fresh games only, a release process, etc.>

## Website

- **Where:** `<site dir>`: <pages>. Live at <URL>.
- **Published:** <how, e.g. "GitHub Pages serves `main:/docs`, so merging to main publishes; a build takes about a
  minute" | "merge to main, then `.\deploy-site.ps1` pushes `site/` to gh-pages">.
- **Look:** "<direction name>". <one sentence of what the site is, as a physical thing>. The look is fixed:
  updates extend it and never restyle it.
- **Design records (read these before any site change):**
  - `PRODUCT.md`: the facts, voice, and every site contract.
  - `DESIGN.md`: the visual system and its named rules, the source of truth for the look.
  - `.impeccable/surfaces/<brief>.md`: the direction contract.
  - `.impeccable/design.json`: tokens and component snippets.
  - `.impeccable/critique/`: the pre-redesign critique.

### Design rules (from DESIGN.md; keep them)

- <each named rule in one line, e.g. "**Two Inks**: aqua #1a6773 and ochre #74520e are the only small-text inks">
- <colour meanings: which colour is reserved for what, and which never appears elsewhere>
- <tokens: the key light/dark values, and where they're defined (`:root`, the dark-theme selectors)>
- Fonts: <font and weights>, self-hosted in `<path>` (OFL, licence file alongside). No other webfonts, and nothing from
  a CDN at runtime.
- Textures and art: <files>, made by `<path>/make_textures.py` (procedural, fixed seeds). Change the script and re-run
  it rather than editing images. Every shipping raster carries provenance: run the Impeccable `embed-prompt` command
  (see below) on each new or changed image.
- Themes: light and dark, via <mechanism and storage key>. Check both.
- Phones: no horizontal scroll at 390px, and tap targets ≥ 44px.
- Motion: <the signature motion>. Everything respects `prefers-reduced-motion`.
- Don't: <the DESIGN.md don'ts: e.g. no nested cards, no side-stripe accents, no gradient text, no new accent
  colours, no stock/generated imagery, no official Timberborn logos or key art>.
- New components: build them from the tokens and components above, match the neighbouring sections, and add them to
  DESIGN.md.

### Content rules

- Describe the mod as it is now. Don't write "New in <version>", "added in …" or version history on player pages;
  that belongs in <the changelog / release notes>.
- The played and not-played status matches the README exactly. Never invent numbers, reviews or screenshots.
- Keep the credits: <credits>. Keep the "unofficial, not affiliated with Mechanistry" line.
- Terminology: <exact terms to use and to avoid>.
- `<release.js path>` is shared across timbermods sites and byte-identical: replace it, never edit it.

### Update the website for a new release

When asked to "update the website for the latest release, consistent with the design":
1. Read the release and the docs: `gh release view <tag> -R <owner/repo>`, README, <changelog>, <design docs>. List
   every player-facing change.
2. Update every place the site states a changed fact:
   - <the list: static release fallbacks (`grep -rn "<old version>" <site dir>`), `data-release-pinned`, status lines,
     requirements, the feature and settings sections, FAQ, troubleshooting, install, og/meta description,
     PRODUCT.md's Operating Context>
3. Put new content into the existing components (<name them: e.g. "a new setting goes in the settings plate list">).
   Don't restyle anything.
4. Test: `<command>` (must pass <n/n>). <other CI checks that touch the site>.
5. Preview: `<command>`, then open <URL>. Capture light, dark and a 390px phone. If the personal
   `impeccable-site-flow` skill is available, use `python <skill>/scripts/capsite.py <URL> <out> "" <pages…>`;
   otherwise use the Browser pane in both colour schemes at desktop and mobile sizes. Check the changed sections and
   that there's no horizontal scroll.
6. Optional but recommended: run the detector,
   `"$(ls -d ~/.claude/plugins/cache/impeccable/impeccable/*/skills/impeccable | tail -1)/scripts/impeccable" detect --json <site dir>`.
   Known false positives: <list>.
7. If the look changed (a new component or layout), update DESIGN.md and `.impeccable/design.json`.
8. Update the README if it repeats the facts.
9. Ship: branch → commit → push → `gh pr create`. After Kyler says merge: `gh pr merge <n> --merge`, then <publish
   step>, then verify:
   - `gh api repos/<owner/repo>/pages/builds/latest -q .status` is `built`;
   - `curl -s <URL> | grep -c "<a changed string>"` finds the change.

### Full redesign

A new look goes through the whole Impeccable flow (init → critique → audit → direction → build → finish review →
DESIGN.md). With the personal skill: "use the impeccable-site-flow skill to redesign this site".
