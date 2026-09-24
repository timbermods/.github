# Meaning contract: seed for MEANING.md

This is the starting point for Dam Good Maps' MEANING.md. It was read from `dev` at `38303f3`, the end of M6 with generator 0.4.0. It describes what the player must be able to read, and what carries each meaning today. Redesign step 3 re-checks every row at HEAD and adds what M7–M11 brought.

Each row says what the style may and may not do. "Word" means visible text or an accessible name, not colour.

## 1. The map (zone M)

The map is data. Its colours are the data palette: they belong to the meaning, not to the design.

### Terrain and water

| Meaning | Carried by today | Where | Rule |
|---|---|---|---|
| Height | A ramp from grass `rgb(122,150,84)` on low ground to dry rock `rgb(196,178,140)` on high ground | `core/render/shade.ts` (pinned: also the `.timber` thumbnail); `render3d/materials.ts` (`0x7a9654`, `0xc4b28c`, rock `0x8c7a5e`) | 2D and 3D agree. `shade.ts` never changes |
| Terraces read as steps | A hillshade lit from the north-west | `shade.ts` | Pinned |
| Clean water and depth | Blue, stronger with depth: `rgb(64,128,200)` in the thumbnail ramp, `rgb(52,112,214)` in the preview's water layer | `shade.ts`, `previewModel.ts` | Blue stays blue. Depth still reads in greyscale |
| Badwater | Brown `rgb(128,84,38)` where contamination is 5% or more. The hover says "Badwater (n%)" | `previewModel.ts` | Never shown by colour alone; the hover word stays |
| Moist soil | A green tint `rgb(60,150,40)`, stronger with moisture | `previewModel.ts` | Must read apart from grass and from forest |
| Soil contamination | A purple tint `rgb(150,60,170)`. The hover says "contaminated" | `previewModel.ts` | See Known collisions |
| Land walkable from the start | A pale tint `rgb(255,248,215)`. The hover says "Walkable from the start" | `previewModel.ts` | |

### Objects on the map

| Meaning | Carried by today | Where | Rule |
|---|---|---|---|
| Trees: species, living or dead | Pine `#1f5a2c` / dead `#6d6450`; Birch `#6fa84a` / `#8b8270`; Oak `#3b7a26` / `#7a705c`; Succulent `#9bb35e`. 3D uses matching crowns and trunks | `Preview2D.tsx`, `entities3d.ts` | Dead trees always read as dead |
| Berry bushes | Purple dots `#8a3fb0` in 2D; a green bush `0x4b6e3c` in 3D | `Preview2D.tsx`, `entities3d.ts` | See Known collisions |
| Ruins and their height | Squares shaded by height: `rgb(110+14h, 80+4h, 70+6h)` | `Preview2D.tsx` | |
| Water and badwater sources | Blue `#1c4fe0` in 2D; `0x2f64d8` and badwater `0x7a4f22` in 3D | `Preview2D.tsx`, `entities3d.ts` | |
| Slopes, and which way is up | Yellow arrows `#f6e27a` pointing uphill | `Preview2D.tsx` | The arrow's direction is the meaning |
| The start | A white outline and an entrance arrow | `Preview2D.tsx` | |
| The best dam site | An orange line `#ff8a1f`, the reservoir it holds, and a label with its volume ("water behind a n-tile dam") | `Preview2D.tsx` | The volume text stays |

### Feature outlines and labels

| Meaning | Carried by today | Where | Rule |
|---|---|---|---|
| Features | Outlines with hover labels: forest `#2f6b2f`, berry patch `#7a3fa0`, ruin field `#8a5a44`, river `#2a64c8`, lake or reservoir site `#3aa0c8`, dam site `#e07a1f`, falls a white marker "Falls, n levels" | `previewModel.ts` | Labels are the meaning. Lake and reservoir site differ only by label |

### Rules for the whole map

| Meaning | Carried by today | Where | Rule |
|---|---|---|---|
| Direction | North up in the top-down views. A compass is always visible in the editor | EDITOR_PLAN §4 | Never rotate. Claude uses the same directions |
| Exact tiles | Whole-number scaling, 1–8×, with no smoothing | PLAN §14.2 | |
| Where the preview is exact | A "preview approximate" overlay under caves and overhangs on imported maps | EDITOR_PLAN §6 | |

The map is identical in light and dark themes. Legends use the same palette module as the canvases.

## 2. Judgement: validation and health

| Meaning | Consequence | Carried by today | Rule |
|---|---|---|---|
| Error (load class) | Blocks export until fixed | The report, the export dialog, the health pill | Heaviest weight. Word plus colour plus icon |
| Warning (playability or design) | Export allowed after a clear confirmation; noted in the map's description | "Warnings", "n warnings" | Clearly lighter than an error, clearly heavier than an advisory |
| Advisory (for example `plants.drought`) | Never blocks | The report. Today it counts in the summary as a warning ("All n checks passed, 1 warning") | Keep it as it is. It fires on every River Valley map (pending decision #2). Making it read apart from warnings is a meaning change for Kyler, and a likely one |
| Not applicable | Nothing | The report | Quiet |
| An imported map's own problems | Listed apart; never block; never noted in the description (D43) | "Already in the map when you opened it" | Never blamed on the player's edits |
| All clear | Export freely | "All n checks passed", "Ready to play" | Shown only when true |
| A fix exists | One click, previewed, undoable | Fix buttons | A fix is an edit: it goes into the history |
| Where the problem is | Clicking an issue moves the camera to it | EDITOR_PLAN §6 | Under reduced motion, a jump |

Visual weight follows consequence: error, then warning, then advisory, then not applicable. The report keeps the grouping of PLAN §11.6. Where today's app gives two of these the same weight, record it and don't change it without Kyler.

## 3. Process: what is happening now

| Meaning | Carried by today | Rule |
|---|---|---|
| The preview is out of date after a settings change | Stale marking, with "Generate" offered (PLAN §14.1) | A stale preview never looks fresh. Word, not only fading |
| Generating, or the water settling | "Working…" (0.4–0.8 s at 256²) | Honest: shown while the work runs, gone when it ends |
| A tool is planning | "Planning…" | Same |
| Background checks pending (M8) | Per M8 | Never shows "Ready to play" early |
| A copy happened | "Link copied." | Announced to screen readers |
| Autosave and restore | The reload reopens the map with its edits | The restore offer names the map |

## 4. Plans and reports: "see it before you commit"

| Meaning | Carried by today | Rule |
|---|---|---|
| What a tool will do, before it does it | The plan drawn on the map with its report, then **Place** applies it as one step | The plan reads as not yet applied |
| The map can't take what was asked | Reductions: "Width 20 reduced to 19, the largest this map allows" | Reduction text stays whole and visible |
| Refused, and why | The plan's report gives the reason (loops, hairpins, through the start's area, near another mouth, across a riverside pond) | The reason is shown, never only a disabled button |
| The start's spot is good or bad | Footprint green or red, plus water, trees and berries in reach | Red and green also differ in words or shape |
| What a crossing river does | Its report says it takes the other river's water (pending decision #13) | Stays in the report |

## 5. Ownership and history

| Meaning | Carried by today | Rule |
|---|---|---|
| Generated, or made by the player | "yours" in feature names (for example "forest yours") | Word, not tint alone |
| Made by Claude (M12) | To come | Add a word when M12 lands |
| Locked areas (M11), and what locks keep | To come | |
| Orphaned edits | Kept and reported | Never hidden |
| History | Plain labels: "Add forest", "Move start", "Change settings and regenerate" | Wording is meaning |
| Edits survive regeneration | "Your n edits stay" | |

## 6. Reference: how this map compares

| Meaning | Carried by today | Rule |
|---|---|---|
| Official maps' range for a setting | A faint band on each control: "official maps: 4–35 sources" (PLAN §14.1) | The band and its words stay legible in both themes |
| Score against official maps | Component bars with the official range (PLAN §14.3) | Stays |
| Settings blocked, and why | Disabled with the reason (for example a drought reserve too big for the map) | The reason is visible |

## 7. Language

- **Four ideas:** **Land**, **Water**, **Resources**, **Start** (EDITOR_PLAN §1, principle 5).
- **Plain words** in simple mode, with exact numbers in advanced mode. Units always show: levels, tiles, water/s.
- **Labels the browser tests use** (verify at HEAD):
  - **Refine this map**, **Generate, keeping my edits**, **Place**, **Done**, **Export**, **Export .timber**, **Top-down**, **History**;
  - the tabs **Land**, **Water**, **Resources**, **Start**;
  - the tools **River** and **Start**;
  - the fields **Width (tiles)** and **Drop (levels)**;
  - the texts "All n checks passed", "Warnings", "Best dam site", "Link copied.", "Planning…";
  - the panels "Preview" and "<feature>, selected".
- **Renaming any of these is a meaning change.** It ripples into the tests, README, install help, the plans and Claude's vocabulary.

## 8. Contracts

These are not visible meanings, but a restyle must not break them.

- The URL fragment: keys and values, PLAN §14.5.
- The project file (`.damgoodmaps.json`, format 2).
- The IndexedDB database (`src/platform/index.ts`).
- Download names: `<name> (<seed>).timber`, plus the "Without pre-filled water" copy.
- The worker API (`src/worker/api.ts`).
- Every sha256 the tests pin.
- New with this flow: the theme key `damgoodmaps.theme`.

## 9. Truth and status

- The in-game checks are pending (`docs/ingame-log.md`). Nothing says or implies "tested in game" until they pass.
- Timberborn 1.1 is the target. The app is unofficial and not affiliated with Mechanistry.
- Keep the credits the README keeps.
- Install help must match PLAN §14.4, including the artifact edition's `.zip` step (D10).

## Known collisions

Record these, don't fix them silently. Any fix is a meaning change for Kyler.

- **Berries and contamination share a purple.** Berry dots `#8a3fb0` and the contamination tint `rgb(150,60,170)` differ only by form: dots versus a tint.
- **Five blues.** The water blues (`shade.ts`, the preview's water layer), source markers `#1c4fe0` and `0x2f64d8`, and the river outline `#2a64c8` all sit close together.
- **Two white marks.** The start and the falls marker are both white, told apart by shape and label.
- **Two orange dam marks.** The best dam site `#ff8a1f` and the dam-site outline `#e07a1f` are near each other, told apart by the volume label.
- **The placeholder UI borrows the hub's colours.** Pine green `#2f5d3a` is the accent, and the night surfaces are forest floor and moss (`src/styles/app.css`). The redesign replaces them. Pine is the hub's own.
