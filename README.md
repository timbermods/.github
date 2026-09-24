# .github

Organization-wide files for [Timbermods](https://github.com/timbermods).

`profile/README.md` is the page shown at <https://github.com/timbermods>. This file is not shown there.

## Layout

| Path | Purpose |
| --- | --- |
| `profile/README.md` | The organization profile: banner, the mods, install steps |
| `profile/banner.svg` | The header image |
| `profile/cards/*.png` | One 640 x 400 picture per mod: its picture from the [catalog](https://timbermods.github.io/) in a sleeve, framed in the mod's colour |
| `profile/make_images.py` | Renders those pictures (`profile/src/` holds its textures and font) |
| `claude-skills/impeccable-site-flow/` | The Claude Code skill that designed every Timbermods website, and keeps each one current |

## Adding a mod

1. Add the mod to the [catalog](https://github.com/timbermods/timbermods.github.io) first; its picture and accent colour come from there.
2. Add it to `CARDS` in `profile/make_images.py` (its id, accent and category) and run `python profile/make_images.py` (Python with playwright, and Microsoft Edge installed). Re-run it whenever a mod's picture changes in the catalog.
3. Copy one `<td>` block in `profile/README.md` into the right group (Play together, Big colonies, Build and plan, as in the catalog), then change the image, links, text and accent colour. Keep the text the same as the catalog's. The version badge follows the repository's latest release by itself, so no version is written by hand.
4. If the repository has only pre-releases, keep `&include_prereleases` in its version badge and the **Preview** badge. Once it has a stable release, remove both.

Image links in the profile are absolute `raw.githubusercontent.com` URLs, so they load wherever the profile is rendered.

## The website design flow (Claude Code)

`claude-skills/impeccable-site-flow/` holds the Impeccable flow that designed every Timbermods website. It has two
modes:

- **Redesign:** init, critique and audit, an own direction, the build, a finish review, then DESIGN.md.
- **Update:** bring a site up to date for a new release while keeping its recorded design.

It needs the Impeccable plugin for Claude Code. To install it for your user, copy the folder to
`~/.claude/skills/impeccable-site-flow/`. Each mod repo's `CLAUDE.md` carries that site's own design rules, tests,
preview and publish steps. That is enough for a session to act on "update the website for the latest release,
consistent with the design", even without the skill.
