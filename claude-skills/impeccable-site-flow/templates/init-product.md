You are doing the Impeccable "init" step for one website: write PRODUCT.md, the durable product record that later design work reads. Do not design anything, and edit no file other than this one PRODUCT.md.

REPO WORKTREE: <absolute path> (GitHub <owner/repo>). Website source: <docs/ | site/ | repo root>. Context: <one paragraph: what the mod does, who made it, what it builds on, latest release tag and status, how changes reach main (PR → merge), credits that must appear>.

Read these first, for format and the level of specificity expected (finished examples from sibling sites):
- <path to a finished PRODUCT.md>
- <path to a second finished PRODUCT.md>

Then study THIS repo: README.md, the changelog, developer notes (anything about the website, publishing it, or tests/CI that check it: grep tests/ and .github/workflows/ for site checks and spell out every contract), every page of the current site, the releases (`gh release list -R <owner/repo> -L 10`; `gh release view <latest tag> -R <owner/repo>`), and the images the site already has.

Write PRODUCT.md at the worktree root with this skeleton (copy the schema comment verbatim):
# Product
<!-- impeccable:product-schema 1 -->
## Platform (web)
## Users (who arrives, in what situation, doing what job)
## Product Purpose (what it does in plain words; success in priority order: understand it, install it right, use it, report problems)
## Positioning (truthfully, versus the base game and neighbouring mods)
## Operating Context (current version and status, game version, requirements, compatibility, the in-game controls/settings players meet, reporting path)
## Capabilities and Constraints (where the site source lives and how it's published; EVERY site-test/CI contract spelled out; shared files that must not be edited: release.js is shared across timbermods sites and is replaced, never edited; exact terminology; honest status of what has and hasn't been played in game)
## Brand Commitments (voice: a fellow player explaining a useful mod, clear and exact, never hype; no official Timberborn logos or key art, but the game's own item icons are allowed where used; license; an unofficial community mod, not affiliated with Mechanistry; required credits)
## Evidence on Hand (real screenshots and images with paths; demos; say plainly what does NOT exist and must not be faked)
## Product Principles (3-5, derived from this mod)

The maintainer's standing rules for every site:
- Player pages describe the mod as it is now.
- Version history belongs in the changelog; keep only the upgrade facts players need.
- Be honest about what has been played, without scaring people off.
- Never invent claims.

Return a 6-10 line summary:
- the mod in one sentence;
- its version and status;
- how the site is published;
- every site contract you found (or "none");
- anything left open.
