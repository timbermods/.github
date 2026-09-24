# CLAUDE.md

This repo is timbermods/.github: the organization profile shown at <https://github.com/timbermods>
(`profile/README.md`), the shared Latest-release workflow, and the website design skill in `claude-skills/`.
[README.md](README.md) explains each part, how to add a mod, and how the profile's images are linked.

## Standing rules

- Never launch or drive Timberborn, and never touch installed mods or saves. Kyler playtests himself.
- Commit on a branch and open a PR with `gh pr create --repo timbermods/.github --base main`.
- Never write "card", "binder", "pocket" or "sleeve" in anything a visitor reads, alt text included. The folder name
  `profile/cards/` and `CARDS` in `make_images.py` stay. The look is wood, brown and green.
- Keep every image URL byte for byte unless you are changing that image: the banner and some pictures are linked by
  commit on purpose (README.md, *Adding a mod*).
- Mod names are exact: BeaverBuddies Stability Fork, Timber Together, Late Game Performance, Optimized Local Housing,
  Hungry Pathing, MixedStorage, Persistent Work Areas, The Tipsy Tail.
- Keep the footer's credit to BeaverBuddies by thomaswp and contributors, and the line that Timbermods is unofficial
  and not affiliated with Mechanistry.
- Each mod's tagline, category, accent colour and group match the catalog (timbermods/timbermods.github.io). Its text
  is the opening of its README, short, with facts checked against the mod's code. Writing rules: the next section.
- `README.md` and `profile/README.md` use CRLF line endings; keep them.

## Writing README and website text

Kyler, 2026-09-24: "simplicity and elegance is effective and desirable." Every change to the README, the website
text and the player docs follows these rules.

- **Write for a Timberborn player** who wants to download, install and use the mod. Developer detail goes in
  this repo's `README.md` (not shown on the profile); link to it rather than repeating it.
- **Short.** One idea per sentence, most under about 20 words. A paragraph or FAQ answer is one to three sentences,
  a troubleshooting answer a few numbered steps.
- **Lead with the action.** Menu paths as arrow chains; on-screen labels in bold, exactly as in game.
- **Say each thing once**, where a player would look for it; link to it elsewhere.
- **Plain words.** No internals (class names, ids, formats) unless the player needs them to act.
- **Cut** filler, repeated caveats, edge cases a player won't meet, and history ("since …", "no longer", older
  builds). Describe the mod as it is now.
- **Check every fact against the code** before writing it; changelogs lag.
- **Keep, briefly:** credits, the unofficial line, the status, and safety facts.
- **Reread as a new player before publishing.** Every step works as written, and nothing is said twice.
