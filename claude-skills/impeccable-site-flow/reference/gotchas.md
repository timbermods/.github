# Gotchas learned building the timbermods sites

## Shell and tools (Windows)

- **Python heredocs in Git Bash** break on apostrophes, backslashes and `\d` in regexes ("unexpected EOF", stripped
  backslashes). Write the script to the scratchpad with the Write tool, then run it.
- **Git Bash converts paths** in `origin/main:path` arguments. Prefix the command with `MSYS_NO_PATHCONV=1`.
- **capsite.py takes page names as separate args** (`"" install.html faq.html`). One comma-joined arg captures the 404.
- **`git checkout -b` fails when the branch exists**, and anything chained after it with `&&` silently doesn't run.
  Use `checkout -B`, or check first.
- **Don't poll background agents or tail their output files.** Wait for the completion notification.
- **Stop the preview servers** (python http.server on distinct ports) when you're done.

## Design

- **Class-name collisions:** a `.bar` masthead collided with a chart's `.bar`, and `.key` collided with a tooltip's
  `.key`. Grep a new class name before using it.
- **Flex items won't shrink below their content** (`min-height: auto`). An `aspect-ratio` on an `<a>` that wraps an img
  did nothing. Put the aspect ratio on the img itself.
- **Scale SVG text with the CSS geometry.** You can't move SVG text with CSS on phones, only resize it, so design the
  phone layout's text positions up front.
- **Tile textures show their repeat** when the low-frequency noise is strong. Keep the cloud term small (≤0.3×), use
  N ≥ 512, and add directional grain (nap or fibre). WebP flattens subtle noise, so raise amplitude or quality.
- **An opaque texture ignores its background colour.** A dark theme needs its own texture file, not just a colour
  token.
- **A sheen or gloss overlay at full strength washes out text.** Rest it at about 0.4 opacity, placed over the art.
- **The detector's `cramped-padding` false positives** come from `clamp()` and nested padding, and its flat-type false
  positives from 404 pages that load CSS by absolute path. Triage them against screenshots, and record the lasting ones
  in `.impeccable/config.json` `ignoreValues` with a reason.
- **`side-tab` (a thick one-side accent border) and `border-accent-on-rounded` flags are usually real.** Replace them
  with a device from the world, such as a mini card, a swatch or a rule.
- **Fraunces is flagged as overused.** Pick a face that belongs to the world, and ship only the weights you use.
- **Labels above headings** (a small uppercase kicker over an h3) are banned by the craft floor. Put the question in
  the heading.

## Truthfulness

- **Hero numbers must compare like with like.** Late Game Performance's save-freeze figure was measured against an
  earlier mod build, so it couldn't be labelled "game". Use only numbers that were measured and have a source.
- **Diagrams must match the demo and the mod.** A move-cycle diagram that contradicted the seating demo had to be
  redrawn.
- **Don't claim behaviour the mod doesn't have.** For example, a hunger bar "refilling to full".

## Repos and publishing

- **The hub's `data/releases.json` is written by a bot** (hourly). Never edit it; merge origin/main before a PR.
- **MixedStorage publishes from gh-pages.** After merging, run `deploy-site.ps1` from a checkout of origin/main (it
  publishes the working tree's `site/`).
- **Pages builds take about a minute.** Verify with `gh api repos/<o>/<r>/pages/builds/latest` plus a `curl` grep.
- **HungryPathing's site design records live in `docs/`** (`.impeccable/config.json` `projectRoots: ["docs"]`), apart
  from the mod's own root DESIGN.md.
