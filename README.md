# .github

Organization-wide files for [Timbermods](https://github.com/timbermods).

`profile/README.md` is the page shown at <https://github.com/timbermods>. This file is not shown there.

## Layout

| Path | Purpose |
| --- | --- |
| `profile/README.md` | The organization profile: banner, the mods, install steps |
| `profile/banner.svg` | The header image: a river valley at dusk, a beaver swimming home past its lodge and dam, pines and birches |
| `profile/make_banner.py` | Draws `banner.svg` (fixed seed; the title is Anybody from `profile/src/`, turned into outlines). Needs `pip install fonttools brotli` |
| `profile/avatar/` | The organization's avatar: a pine growing up through a brass gear. `make_avatar.py` draws the SVG; upload `timbermods-avatar-1024.png` at the org's Settings → Profile picture |
| `profile/cards/*.png` | One 640 x 400 picture per mod: its picture from the [catalog](https://timbermods.github.io/) in a sleeve, framed in the mod's colour |
| `profile/make_images.py` | Renders those pictures (`profile/src/` holds its textures and font) |
| `claude-skills/impeccable-site-flow/` | The Claude Code skill that designed every Timbermods website, and keeps each one current |

## Adding a mod

1. Add the mod to the [catalog](https://github.com/timbermods/timbermods.github.io) first; its picture and accent colour come from there.
2. Add it to `CARDS` in `profile/make_images.py` (its id, accent and category) and run `python profile/make_images.py` (Python with playwright, and Microsoft Edge installed). Re-run it whenever a mod's picture changes in the catalog.
3. Copy one `<td>` block in `profile/README.md` into the right group (Play together, Big colonies, Build and plan, as in the catalog), then change the image, links, text and accent colour. Keep the text the same as the catalog's. The version badge follows the repository's latest release by itself, so no version is written by hand.
4. If the repository has only pre-releases, keep `&include_prereleases` in its version badge and the **Preview** badge. Once it has a stable release, remove both.

Image links in the profile are absolute `raw.githubusercontent.com` URLs, so they load wherever the profile is rendered. GitHub's image servers cache those files by path for a few minutes and can ignore a `?v=` query, so a changed image can keep showing the old version. The banner is therefore linked by the commit that holds it (`raw.githubusercontent.com/timbermods/.github/<commit>/profile/banner.svg`): after changing it, merge, then point that link at the new commit. The mod pictures use `?v=` numbers; if one sticks, link it by commit the same way.

## The website design flow (Claude Code)

`claude-skills/impeccable-site-flow/` holds the Impeccable flow that designed every Timbermods website. It has two
modes:

- **Redesign:** init, critique and audit, an own direction, the build, a finish review, then DESIGN.md.
- **Update:** bring a site up to date for a new release while keeping its recorded design.

It needs the Impeccable plugin for Claude Code. To install it for your user, copy the folder to
`~/.claude/skills/impeccable-site-flow/`. Each mod repo's `CLAUDE.md` carries that site's own design rules, tests,
preview and publish steps. That is enough for a session to act on "update the website for the latest release,
consistent with the design", even without the skill.

## When a mod gets a new Latest release

`.github/workflows/latest-release.yml` is a shared workflow every mod repo calls from its own
`.github/workflows/latest-release.yml`; the work is done by `scripts/latest_release.py`. It runs only when a release
becomes GitHub's **Latest**. Pre-releases, drafts and older releases change nothing anywhere. It makes only fixed,
mechanical updates:

1. It appends a standard footer to the release notes, once: an install line, the website and install-guide links, and
   the zip's SHA-256. Anything your notes already have (an Install heading, the checksum) is left out.
2. It sets the website's release fallback text (`data-release="version|tag|asset-name"`) to the new release.
3. It updates the README lines that end with `<!-- latest -->`, replacing the previous Latest version.
4. It runs the site checks (local links resolve, scripts parse, the repo's own site test). If they pass, it commits
   to the default branch and Pages republishes. If they fail, it changes nothing and opens an issue.

Descriptions, status lists, FAQs and the catalog's and this profile's wording stay manual. The catalog's download
buttons and this profile's version badges already follow the Latest release on their own.

To see what it would do without changing anything, run a mod repo's **Latest release** workflow by hand (Actions →
Latest release → Run workflow); its dry run is on by default.

GitHub runs a release's workflow from the commit its tag points to, so a release tagged on a commit from before a
repo had this workflow won't trigger it. For such a release, run the workflow by hand with **dry-run** unticked.

