# State matrix and the capture tool

An app is judged in its states, not its pages. This matrix lists every state the design pass must capture and review. It serves three purposes:
- it gives the ARIA snapshot tests their list;
- it gives the before and after captures their list;
- it is the finish reviewer's checklist.

Update mode adds a row for every new state.

## The capture tool

Add `tools/capture-states.ts`, run with `npx tsx tools/capture-states.ts --out <dir> [--only <state>]`.

- **Driving the app:** it uses Playwright on local Chrome, as the browser tests do (D22), against `vite preview` of a fresh build. It reaches each state with the same role and name locators the tests use, never CSS classes.
- **Inputs:** seed 4242 at 96², the tests' map, plus a 256² map for density.
- **What it captures:** each state in 4 variants: desktop 1440×900 and phone 390×844 (`isMobile`, `hasTouch`), each in light and dark. Every capture runs with reduced motion and waits for "Working…" and "Planning…" to clear.
- **What it saves:**
  - a PNG per state and variant, named `<state>__<viewport>-<theme>.png`;
  - a greyscale copy of each, for the colour-only check;
  - an `index.md` listing every file with its state's meaning row from MEANING.md.
- **Where:** output goes under `.scratch/captures/`, which is never committed (like `.scratch/renders`).
- **Local-only states:** states that need the investigation maps (an imported map with caves) run only when those files are present, and say so in the index when skipped.

## Generator page

| State | How to reach it | What must read |
|---|---|---|
| `gen-ready` | Load, generate 4242 | The map, the card, "All n checks passed", **Refine this map** |
| `gen-stale` | Change one setting without generating | Stale is obvious, with a word; "Generate" offered |
| `gen-working` | Generate 256², capture mid-run | "Working…" |
| `gen-warnings` | A map with a playability or design warning that isn't advisory (find a spec with `tools/batch.ts`, or make one with an edit) | Warning weight and word |
| `gen-advisory` | River Valley at Normal (`plants.drought`). Today the browser tests see it as "All n checks passed, 1 warning" | Whether an advisory reads apart from a warning. Record what it does now; changing it is a meaning change (pending decision #2) |
| `gen-guard-warn` | Hard with a Scarce drought reserve (D13) | The panel's warning, apart from the report |
| `gen-layers-each` | Each layer toggle on alone: water, badwater, moisture, contamination, trees, berries, ruins, start, slopes, dam sites, reach, features | The legend word for each; distinct in greyscale |
| `gen-hover` | Hover water, badwater, moist soil and the dam site | Readout text |
| `gen-3d` | The 2D/3D switch | Same meanings in 3D |
| `gen-settings-sections` | Open each section, including Advanced start rules | Official-range bands and reasons for disabled controls |
| `gen-guard` | A drought reserve too big for the map | The disabled reason |
| `gen-share` | **Copy link** | "Link copied." |
| `gen-download` | Download | Install help, including the artifact edition's `.zip` step when that edition exists |
| `gen-open-import` | Open an official map (local) | The list of normalizations; its own problems listed apart |
| `gen-old-link` | A link with an older `v` (M13, versioned deploys) | The choice: open in the old version, or regenerate |
| `gen-phone-drawer` | Phone, settings drawer open and closed | PLAN §14.1 |

## Editor

| State | How to reach it | What must read |
|---|---|---|
| `ed-open` | **Refine this map** | The map, the four tabs, the health pill, **Export**, undo and redo |
| `ed-tab-<name>` | Each tab: **Land**, **Water**, **Resources**, **Start** | Its tools and feature list |
| `ed-planning` | **River**, click a course | "Planning…", then the plan shown as not yet applied |
| `ed-plan-reduced` | A 20-wide waterfall on 48² | "Width 20 reduced to 19…" |
| `ed-plan-refused` | A river across a riverside pond, or a loop | The reason |
| `ed-selected` | Select a feature | "<feature>, selected", its inspector |
| `ed-start-good` / `ed-start-bad` | Drag the start to a good spot and a bad one | Green and red differ by more than colour; indicators show |
| `ed-issue-list` | An edit that makes a problem | The issue, its fix button, its location |
| `ed-export-clean` | **Export** with no problems | Nothing to confirm |
| `ed-export-warning` | **Export** with a warning | The confirmation, and the note that it goes in the description |
| `ed-export-error` | **Export** with a load error | Blocked, with the reason and the fix |
| `ed-export-import` | Export an unedited official map (local) | "Already in the map when you opened it" |
| `ed-history` | **History** | Plain labels, and the current step |
| `ed-orphans` | Regenerate so that an edit loses its target | The orphan, reported |
| `ed-regenerate` | **Generate, keeping my edits** | "Your n edits stay" |
| `ed-working` | A terrain edit at 256² | "Working…" |
| `ed-approximate` | An imported map with caves (local) | "Preview approximate" |
| `ed-topdown` | **Top-down** | North up; the compass |
| `ed-restore` | Reload with edits | The restore names the map |

M7–M11 rows to add in step 3: the resource tools, thorns, relics, mine sites, geothermal fields, sculpt brushes, naturalize, stamps, symmetry, regenerate area and locks. M12 adds the Claude panel and its states.
