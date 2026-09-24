---
name: impeccable-site-flow
description: Kyler's proven Impeccable website flow for mod/project sites (used for every timbermods site, 2026-09-23). Use it to REDESIGN a site from scratch (init → critique+audit → own direction → build → finish review → DESIGN.md → PR → publish), or to UPDATE an already-designed site for a new release while keeping its recorded design (DESIGN.md). Triggers - "redesign <site> with the impeccable flow", "apply the impeccable flow to <site>", "update the <mod> website for the latest release, consistent with the design".
---

# Impeccable site flow

This is the flow that produced the timbermods sites: Timber Together "River Station Signage", MixedStorage's apothecary
cabinet, the Stability Fork's log round and saw, Late Game Performance's "Pit Crew", Optimized Local Housing's seating
plan, Hungry Pathing's enamel yard signs, Persistent Work Areas' drafting plan, The Tipsy Tail's poolside bar and the
hub's collector's binder. Two modes:

- **Update** (most common): the site already has PRODUCT.md, DESIGN.md and `.impeccable/`. Bring content up to date
  (a new release, changed features) and keep the look exactly as recorded. → [Update mode](#update-mode)
- **Redesign**: a site gets its own new visual world. → [Redesign mode](#redesign-mode)

For a working web app such as Dam Good Maps, use the `impeccable-app-flow` skill instead.

Each repo's `CLAUDE.md` carries that site's specifics: where it lives, tests, preview, publishing and design rules.
Read it first, and follow it wherever it's more specific than this skill.

## Standing rules (Kyler's, for every site)

- **Never launch, drive or auto-test Timberborn**, and never touch installed mods or saves. Kyler playtests himself.
- **The site describes the mod as it is now.** Don't write "New in", "added in <version>", or version history on player
  pages; that belongs in the changelog and release notes. Upgrade facts players actually need are the only exception.
  Assume fresh games: don't write about old-save compatibility (unless the repo's CLAUDE.md says otherwise).
- **Be honest about status.** Played/not-played lines match the README exactly. Don't scare people off and don't
  overclaim. Never invent numbers, testimonials, download counts or screenshots.
- **No official Timberborn logos or key art.** Game item icons are allowed where a site already uses them. Keep every
  credit (BeaverBuddies by thomaswp, GPL, and similar).
- **`release.js` is shared across most timbermods sites** and byte-identical there. Replace it, never edit it.
  Timber Together runs its own variant; Persistent Work Areas and the hub use their own `site.js`. Each repo's CLAUDE.md
  says which applies.
- **Write short and plain** (Kyler, 2026-09-24: "simplicity and elegance is effective and desirable"). Every README
  and site text change is for a Timberborn player who wants to download, install and play:
  - one idea per sentence, most under about 20 words;
  - one to three sentences per paragraph or FAQ answer, a few numbered steps per troubleshooting answer;
  - lead with the action and write menu paths as arrow chains (Load game → pick a save → **Host co-op game**);
  - bold on-screen labels, spelled exactly as in the mod's English strings;
  - say each thing once and link to it elsewhere;
  - no internals (classes, ids, messages between computers), filler, repeated caveats or history ("since …", "no longer");
  - check every flow against the code before writing it, since changelogs lag;
  - reread as a new player before publishing.

  Developer detail goes in a DEVELOPING.md or the changelog, not the README. Timber Together's copy pass (PR #22) is
  the model.
- **No smoke, smear, dust, sheen or glare textures** over content, boards or pictures (Kyler, 2026-09-24: Hungry
  Pathing's chalk-smeared slate "looks like smoke", the profile's sheen "looks awful"). Surfaces are flat colours or
  quiet grain; a dark-mode surface must be dark (no cream panels on a night page).
- **Tooltips in Mod Settings don't wrap** (≤112 chars per line). That only matters if site copy is reused in game.
- **Once a plan is agreed, keep going to the end** (build → review → fix → PR → publish) without pausing. Ask only real
  product decisions. Merging needs Kyler's say-so in chat, because the auto-mode classifier blocks `gh pr merge`
  otherwise. When he has said so, merge, publish, and verify live.

## Tools

- **Impeccable launcher:** `IMP=$(ls -d ~/.claude/plugins/cache/impeccable/impeccable/*/skills/impeccable | tail -1)`,
  then `"$IMP/scripts/impeccable" <verb>`. Its references are in `$IMP/reference/` (critique.md, audit.md,
  new-work.md, craft-floor.md, polish.md, …). Read `craft-floor.md` before any UI edit.
  - `context --target <file>`: loads PRODUCT.md, DESIGN.md and the surface brief.
  - `detect --json <dir>`: the anti-pattern detector. Parse output from the first `[` or `{`.
  - `concept-seed --scope direction --mode persuade`, then `concept-seed ... --kind assigned --from <key>` to record the pick.
  - `surface-brief write <target> <brief-file>`: stores the direction contract.
  - `critique-storage write "file:<path>" <body-file>`: stores the critique snapshot.
  - `embed-prompt <raster> --prompt "Origin: ..."`: records provenance for a shipping image; `embed-prompt --scan .` checks that none is missing.
- **Agents:** `general-purpose` for critique A and B; `impeccable:impeccable-finish-reviewer` for the finish review (at
  most 2 rounds; continue the same agent with SendMessage); `impeccable:impeccable-documenter` for DESIGN.md and
  `.impeccable/design.json`.
- **Captures:** `python scripts/capsite.py <base-url> <out-dir> "" page2.html page3.html` (from this skill's folder;
  pages are SEPARATE args and the first is `""`). It writes desktop / desktop-dark / mobile / mobile-dark full pages plus
  `-top` crops and prints horizontal overflow. It uses Playwright on installed Edge (`channel="msedge"`, true
  `is_mobile` 390px), because headless Edge ignores widths under ~500px. View captures by cropping them with Pillow;
  full pages are too tall to read whole.
- **Preview server:** `python -m http.server <port> -d <site-dir>` (run in the background), or the repo's own server.
  Use a distinct port per site.
- **Fonts:** self-host OFL fonts from
  `https://cdn.jsdelivr.net/npm/@fontsource/<font>/files/<font>-latin-<weight>-normal.woff2`, and put the OFL text next
  to them (from github.com/google/fonts `ofl/<font>/OFL.txt`). Ship only the weights you use.
- **Textures and art:** procedural, with numpy and Pillow and fixed seeds, in a `make_textures.py` beside the output
  (see `scripts/make_textures_example.py`). Then `embed-prompt` each output. Never use generated or stock imagery.

Gotchas are in `reference/gotchas.md`; read it before building.

This skill is backed up in `timbermods/.github` under `claude-skills/impeccable-site-flow/`. When you improve it, update both
copies, through a PR to that repo.

## Update mode

For "update the <mod> website for the latest release, consistent with the design".

1. **Read the records.** The repo's CLAUDE.md, then PRODUCT.md (facts, every site contract), DESIGN.md (the visual
   system and its named rules) and `.impeccable/surfaces/*.md` (the direction contract). Don't restyle anything. The
   design is fixed; you extend it only with its own tokens and components.
2. **Learn what changed.** `gh release list -R <owner/repo> -L 5`, `gh release view <tag> -R <owner/repo>`, the
   README, the changelog and design docs. List every player-facing fact that changed: version strings, game version,
   requirements, features, settings, controls, played/not-played status, limits, install steps.
3. **Find every place the site states those facts.** Grep the site for the old version, setting names and feature
   names, including static fallbacks for release.js (`data-release`, `data-release-pinned`), status lines, FAQ,
   troubleshooting, install, 404 and og text. Update PRODUCT.md's facts too.
4. **Edit the content in the existing components.** A new feature goes into the section and component that already
   hold its kind; copy an existing block's markup. If nothing fits, build the smallest new component from DESIGN.md's
   tokens and type ramp, then add it to DESIGN.md's components section. Keep the voice in PRODUCT.md. Remove claims
   that stopped being true.
5. **Test.** Run the repo's site test or validator (see CLAUDE.md) and any tests CI runs on the site.
6. **Look.** Start the preview, run capsite.py (all pages; light, dark and phone), and check overflow 0, the changed
   sections, and anything that moved. Run `detect --json <site-dir>` and triage findings against the repo's
   `.impeccable/config.json` ignores and CLAUDE.md's known false positives.
7. **Review, if the change is visual** (a new component or a changed layout): one round of
   `impeccable:impeccable-finish-reviewer` against the surface brief and DESIGN.md. Fix what's material.
8. **Keep the records true.** If a component or token changed, update DESIGN.md and `.impeccable/design.json`
   (re-run the documenter for big changes). Update the README if it repeats the facts.
9. **Ship.** Commit on a branch → push → `gh pr create`. Merge when Kyler has said to, then run the repo's publish step
   and verify live (see CLAUDE.md: Pages build status plus a `curl` of the live page for a changed string).

## Redesign mode

For a new site, or "redesign <site> with the impeccable flow". Tailor every prompt to the site: its README, releases,
audience, install facts and status. The templates in `templates/` are the ones that worked; fill every `<…>` field.

1. **Setup.** Make a worktree on a new branch (for example `claude/site-redesign`). Find the site dir, publish path,
   tests and CI checks, and start a preview server.
2. **Init.** Write PRODUCT.md with a general-purpose agent and `templates/init-product.md`, using two finished
   PRODUCT.md files as examples. Read and correct its summary: every contract, and the honest status.
3. **Critique and audit.** Launch two agents in parallel: `templates/critique-a.md` (design review, three tailored
   tests) and `templates/critique-b.md` (site test, detector, a11y/mobile/perf audit, inventory). Merge both into one
   snapshot and store it with `critique-storage write`.
4. **Direction.**
   - Run `concept-seed --scope direction --mode persuade`, and build candidates grounded in the mod's own world (what
     the mod does, in physical objects). Exclude any direction a sibling site already uses; every site gets its own
     look.
   - Pick one and record it with `--kind assigned --from <key>`.
   - Write the direction contract with `templates/direction-contract.md` (THESIS / OWN-WORLD / STORY / FIRST VIEWPORT /
     FORM / FINISH) and store it with `surface-brief write`.
   - When the user wants to choose, show 2–3 candidates and wait. Otherwise decide and report.
5. **Build.**
   - Read `$IMP/reference/new-work.md` and `craft-floor.md`.
   - Fonts: self-hosted OFL. Textures: procedural, with provenance.
   - Keep every test hook, id, anchor and contract from PRODUCT.md. Both themes. Tap targets ≥44px. Reduced motion
     respected. No horizontal scroll at 390px.
   - Rewrite the copy to the standing rules. Move version history out.
6. **Verify once.** Tests, capsite (all pages), and the detector; fix everything in one batch.
7. **Finish review.** `impeccable:impeccable-finish-reviewer` with `templates/finish-review.md`. Round 2 is the same
   agent via SendMessage, listing what you changed and any deliberate deviations with the reason. After two rounds, fix
   the remaining items yourself.
8. **Document.** `impeccable:impeccable-documenter` with `templates/documenter.md`. Fix any real defects it reports,
   and sync DESIGN.md and design.json if you change something.
9. **Records and repo.**
   - Add `.impeccable/.gitignore`: `review/`, `questions/`, `live/`, `mocks/`, `hook.cache.json`, `config.local.json`.
   - Update the README's site notes.
   - Add or update the repo's CLAUDE.md website section from `reference/claude-md-template.md`.
10. **Ship.** Commit (`Co-Authored-By` line per the session), push, then `gh pr create` with `templates/pr-body.md`.
    After Kyler says merge: merge, publish, and verify live.

## Adding the flow to a new repo

Copy `reference/claude-md-template.md` into the repo's CLAUDE.md and fill it in from PRODUCT.md and DESIGN.md: the
named rules, tokens, fonts, test, preview and publish commands, the release-update checklist, and known detector false
positives. That makes "update the website for the latest release, consistent with the design" work in any session.
`reference/timbermods-sites.md` lists the current sites.
