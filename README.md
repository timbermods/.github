# .github

Organization-wide files for [Timbermods](https://github.com/timbermods).

`profile/README.md` is the page shown at <https://github.com/timbermods>. This file is not shown there.

## Layout

| Path | Purpose |
| --- | --- |
| `profile/README.md` | The organization profile: banner, mod cards, install steps |
| `profile/banner.svg` | The header image |
| `profile/cards/*.svg` | One 16:10 card image per mod, in the same style as the [catalog](https://timbermods.github.io/) cards |
| `assets/avatar.png` | The organization picture (upload it under Settings > Profile; GitHub has no API for it) |
| `assets/logo.svg` | The tree-ring mark on its dark tile, the same as the catalog favicon |

## Adding a mod

1. Add its card image to `profile/cards/`, 640 x 400, with the accent colour's 4 px bar along the bottom.
2. Copy one `<td>` block in `profile/README.md`, then change the image, links, text and accent colour. The version badge follows the repository's newest release by itself, so no version is written by hand.
3. If the repository has only pre-releases, keep `&include_prereleases` in its version badge and the **Preview** badge. Once it has a stable release, remove both.

Image links in the profile are absolute `raw.githubusercontent.com` URLs, so they load wherever the profile is rendered.
