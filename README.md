# .github

Organization-wide files for [Timbermods](https://github.com/timbermods).

`profile/README.md` is the page shown at <https://github.com/timbermods>. This file is not shown there.

## Layout

| Path | Purpose |
| --- | --- |
| `profile/README.md` | The organization profile: banner, mod cards, install steps |
| `profile/banner.svg` | The header image |
| `profile/cards/*.svg` | One 16:10 card image per mod, in the same style as the [catalog](https://timbermods.github.io/) cards |
| `claude-skills/impeccable-site-flow/` | The Claude Code skill that designed every Timbermods website, and keeps each one current |

## Adding a mod

1. Add its card image to `profile/cards/`, 640 x 400, with the accent color's 4 px bar along the bottom.
2. Copy one `<td>` block in `profile/README.md`, then change the image, links, text and accent color. The version badge follows the repository's latest release by itself, so no version is written by hand.
3. If the repository has only pre-releases, keep `&include_prereleases` in its version badge and the **Preview** badge. Once it has a stable release, remove both.

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
