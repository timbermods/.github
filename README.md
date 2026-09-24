# .github

Organization-wide files for [Timbermods](https://github.com/timbermods). `profile/README.md` is the page shown at
<https://github.com/timbermods>; this file is not shown there.

## Layout

| Path | Purpose |
| --- | --- |
| `profile/README.md` | The organization profile: banner, the mods, install steps |
| `profile/banner.svg` | The header image: a beaver valley at dusk, with its lodge and dam, pines and birches |
| `profile/make_banner.py` | Draws `banner.svg` with a fixed seed; the title is Anybody from `profile/src/`, as outlines. Needs `pip install fonttools brotli` |
| `profile/avatar/` | The organization's avatar: the Timbermods pine on a cut log end, on forest green. `make_avatar.py` draws the SVG; upload `timbermods-avatar-1024.png` at the org's Settings → Profile picture |
| `profile/cards/*.png` | One 640 × 400 picture per mod, from the [catalog](https://timbermods.github.io/), framed in the mod's colour |
| `profile/make_images.py` | Renders those pictures (`profile/src/` holds its textures and font) |
| `claude-skills/impeccable-site-flow/` | The Claude Code skill that designed every Timbermods website and keeps each one current |
| `claude-skills/impeccable-app-flow/` | The Claude Code skill for designing an app (Dam Good Maps) without losing what it means |
| `.github/workflows/latest-release.yml`, `scripts/latest_release.py` | The shared Latest-release workflow ([below](#when-a-mod-gets-a-new-latest-release)) |

## Adding a mod

1. Add the mod to the [catalog](https://github.com/timbermods/timbermods.github.io) first. Its picture, category and
   accent colour come from there.
2. Add it to `CARDS` in `profile/make_images.py` (id, accent, category) and run `python profile/make_images.py`. It
   needs Python with playwright, and Microsoft Edge. Re-run it whenever a mod's picture changes in the catalog.
3. In `profile/README.md`, copy one `<td>` block into the right group (Play together, Big colonies, Build and plan, as
   in the catalog). Change its picture, links, accent colour and text. The tagline matches the catalog's; the text is
   the opening of the mod's README, kept short ([CLAUDE.md](CLAUDE.md)). The version badge follows the latest release
   by itself.
4. A repository with only pre-releases keeps `&include_prereleases` in its version badge, and the **Preview** badge.
   Remove both once it has a stable release.

Image links are absolute `raw.githubusercontent.com` URLs, so they load wherever the profile is shown. GitHub's image
servers cache them by path for a few minutes and can ignore a `?v=` query. So the banner, and any picture that keeps
showing an old version, is linked by the commit that holds it
(`raw.githubusercontent.com/timbermods/.github/<commit>/profile/banner.svg`): after changing it, merge, then point the
link at the new commit. The other pictures use `?v=` numbers.

## The website design flow (Claude Code)

`claude-skills/impeccable-site-flow/` holds the Impeccable flow that designed every Timbermods website. It has two
modes:

- **Redesign:** init, critique and audit, an own direction, the build, a finish review, then DESIGN.md.
- **Update:** bring a site up to date for a new release, keeping its recorded design.

It needs the Impeccable plugin for Claude Code. To install it for your user, copy the folder to
`~/.claude/skills/impeccable-site-flow/`. Each mod repo's `CLAUDE.md` carries that site's design rules, tests, preview
and publish steps, so a session can update a site for the latest release even without the skill.

`claude-skills/impeccable-app-flow/` is the same flow, changed for a working web app such as Dam Good Maps. Meaning
comes first: MEANING.md outranks DESIGN.md, and guard tests freeze the meaning before any restyle. It splits the app
into three zones: frame, instruments and map. Install it the same way, to `~/.claude/skills/impeccable-app-flow/`.

## When a mod gets a new Latest release

Each mod repo calls the shared workflow `.github/workflows/latest-release.yml` from its own
`.github/workflows/latest-release.yml`; `scripts/latest_release.py` does the work. It runs only when a release becomes
GitHub's **Latest**. Pre-releases, drafts and older releases change nothing. It makes four mechanical updates:

1. It appends a standard footer to the release notes, once: an install line, the website and install-guide links, and
   the zip's SHA-256. Parts the notes already have (an Install heading, the checksum) are left out.
2. It sets the website's release fallback text (`data-release="version|tag|asset-name"`) to the new release.
3. It updates the README lines that end with `<!-- latest -->`, replacing the previous Latest version.
4. It runs the site checks (local links resolve, scripts parse, the repo's own site test). If they pass, it commits to
   the default branch and Pages republishes. If they fail, it changes nothing and opens an issue.

Descriptions, status lists, FAQs, and the catalog's and this profile's wording stay manual. The catalog's download
buttons and this profile's version badges follow the Latest release by themselves.

To see what it would do, run a mod repo's **Latest release** workflow by hand (Actions → Latest release → Run
workflow); dry run is on by default. A release tagged on a commit from before the repo had this workflow won't trigger
it, because GitHub runs the workflow from the tagged commit. For such a release, run it by hand with **dry-run**
unticked.
