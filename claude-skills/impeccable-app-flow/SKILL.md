---
name: impeccable-app-flow
description: Kyler's Impeccable design flow, changed for a working web app. Built for Dam Good Maps (the ROADMAP M13 design pass), and usable for any later timbermods app. Redesign mode gives the app a recorded look of its own; update mode builds new UI in an app that already has DESIGN.md and MEANING.md. Both keep everything the app means: every map colour, state, severity, label and contract. Use this whenever someone asks to restyle, redesign, theme, polish or "apply the impeccable flow" to Dam Good Maps, its generator page or its editor, runs the M13 design pass, or adds UI to Dam Good Maps after its design exists. For static mod sites, use impeccable-site-flow instead.
---

# Impeccable app flow

This is impeccable-site-flow, changed for an app. A mod site is read once; an app is worked in. So the site flow's first goal, a look of its own, comes second here. The first goal is that nothing the app means is lost.

Read impeccable-site-flow's SKILL.md and `reference/gotchas.md` first. Its tools, fonts, textures, agents and standing rules apply here unless this file says otherwise. This skill lives beside it in `timbermods/.github/claude-skills/`.

## What changes for an app

| | Site flow | App flow |
|---|---|---|
| What is judged | Pages | Tasks and states: every surface in every state it can be in |
| Records | PRODUCT.md, DESIGN.md | PRODUCT.md, **MEANING.md**, DESIGN.md. Meaning wins over design |
| Where the look goes | Everywhere | The frame. Instruments stay calm. The map is never styled |
| Captures | `capsite.py` on pages | `tools/capture-states.ts`, which drives the app through the state matrix |
| Tests | Keep every hook | Freeze meaning in guard tests first, then restyle against them unchanged |
| Motion | None | Only motion that shows state, with a reduced-motion form |
| Targets | 44px everywhere | 44px in the frame and the phone layout; at least 24px in desktop instruments |
| Publishing | Pages | Pages from `main`, plus the artifact edition's single HTML file |

## Order of authority

1. **The plans:** PLAN.md, EDITOR_PLAN.md, FORMAT.md and the decisions in PLAN §20. They say what the app does.
2. **MEANING.md:** what each colour, mark, word and state tells the player. It is derived from the plans. If it disagrees with them, fix MEANING.md.
3. **DESIGN.md:** the look. It serves meaning. When a design rule and a meaning conflict, the meaning stays and DESIGN.md changes.
4. **Taste.**

## Hard limits

These hold in both modes. No direction, critique or finish review overrides them.

- **No map changes.** Never touch `src/core/**`: the generator, validators, formats and water simulation. Never touch `prototype/` (the Python oracle). A style pass changes no map.
- **`src/core/render/shade.ts` is pinned.** It colours the 2D preview and the 960×540 thumbnail inside every `.timber`. A colour change there changes every file's bytes.
- **No generator version bump,** and no change to any sha256 the tests pin.
- **Contracts stay byte for byte:** the URL fragment's keys and values (PLAN §14.5), the project file, the IndexedDB database, download names (`<name> (<seed>).timber`), and the worker API.
- **No state by colour alone.** Every state and severity has a word. Words survive every restyle.
- **Nothing on the map or behind numbers:** no texture, gradient, glow or overlay on the 2D preview, the 3D view, report text or figures.
- **Test hooks stay.** Never remove or rename a role or accessible name the tests use. A renamed label is a meaning change.
- **No restyling during a milestone run** on the same branch. Its agents edit the same components.
- **The site flow's standing rules hold:**
  - never launch Timberborn;
  - be honest about status (pending in-game checks mean the app never says "tested in game");
  - no official Timberborn logos or key art, and no generated or stock imagery;
  - follow the writing rules in the repo's CLAUDE.md;
  - merging needs Kyler's say-so in chat.

## Three zones

Every element belongs to one zone. The zone decides what the style may do to it.

- **Map (M):** the 2D preview, the 3D view, their overlays and handles, the compass, and the map legend.
  - Colours come from the data palette only, never from design tokens.
  - The map looks the same in light and dark. Only its surround changes.
  - North is up. The 2D preview scales by whole numbers without smoothing, so tiles stay exact.
  - Any change in this zone is a meaning change.
- **Instruments (I):** everything used while working:
  - the settings controls and their official-range bands;
  - the map card, score bars and validation report;
  - the editor's tabs, tool panels, plan reports and inspector;
  - the health pill, issue list, fix buttons, export dialog and history;
  - the hover readout and progress.

  Surfaces are flat, from tokens. Text is the system UI face. Numbers use tabular figures and always show their unit. The world appears only in small, quiet ways, such as a rule, a numeral face or a corner.
- **Frame (F):** the masthead, the ground around the panels, install help, first-run and empty states, the footer with credits, and the 404. This is where the world lives: textures, display type and the signature device.

Hero and example imagery comes from the generator itself: a real map, captioned with its seed and settings. Never draw something that looks like generator output.

## Meaning changes

A meaning change is any change to:
- a zone M colour, mark or legend;
- a label, tab name or unit;
- which states exist, or how they read;
- the order or consequences of severities;
- the compass or north.

The flow may propose meaning changes. It never makes one alone. Each goes in the PR's **Meaning changes** table (`templates/pr-body-app.md`) with before, after, reason, and the tests and docs updated with it. Kyler approves each one.

Adding meaning is allowed, and it is still listed. Examples: a missing legend entry, a word beside a mark that was colour only, or a clearer reason text.

A renamed label ripples into the tests, the README, install help, the plans and Claude's vocabulary. M12's Claude uses the same feature names and directions. Change all of them together, or none.

## Redesign mode

For the M13 design pass, or "apply the impeccable flow to Dam Good Maps".

1. **Gate.** Start only when all of these hold:
   - M11 is done, so the editor's full set of panels exists;
   - no milestone run is working on the branch;
   - CI is green.

   The generator version stays fixed for the whole pass. Ask Kyler whether the pass comes before or after M12. If before, M12 builds its Claude panels in update mode.
2. **Setup and baseline.** Make a worktree on `claude/design-pass` from `dev`. Then record the "before" state:
   - run the typecheck, `npm test`, `npm run test:e2e` (locally, so the investigation maps run), `npm run oracle`, `npm run bench` and `npm run bench:3d`, and save the results;
   - record the sha256 of seed 4242 at 96² and 128² for every theme, using `tools/gen.ts`;
   - capture the state matrix (`reference/state-matrix.md`) into `.scratch/captures/before/`.
3. **Records.**
   - **PRODUCT.md:** use the site flow's `templates/init-product.md`. The audience is players who make and play maps. The contracts section copies this skill's hard limits. The status covers the pending in-game checks and the beta.
   - **MEANING.md:** start from `reference/meaning-contract.md`. Re-check every row against the code at HEAD. Add what M7–M11 brought: the resource tools, thorns, relics, mine sites, geothermal fields, sculpting, stamps, symmetry, regenerate area, locks and orphans.
   - Ask Kyler to confirm MEANING.md once. It is the only step that waits for him before building, because it defines what "lost meaning" means.
4. **Freeze meaning.** Land one PR before any restyle. It must be green on the current look:
   - **The capture tool:** `tools/capture-states.ts` (`reference/state-matrix.md`).
   - **ARIA snapshots:** one browser test per state in the matrix, using Playwright's `toMatchAriaSnapshot` with stored snapshot files. Use regexes for counts and timings. These tests pin every role, name, state word and report line.
   - **One data palette module:**
     - Move every zone M colour outside `shade.ts` into `src/ui/mapPalette.ts`. Today they are in `Preview2D.tsx`, `previewModel.ts`, `render3d/materials.ts` and `render3d/entities3d.ts`.
     - The 3D view and the legends read from the module too.
     - `shade.ts` stays where it is. The module lists its colours as pinned.
     - Prove the move changes nothing: hash the 2D preview's pixels for fixed seeds, before and after.
   - **The palette test** (`tests/unit/mapPalette.test.ts`):
     - Measure the OKLab distance between every pair of data colours that can touch. Do this in normal vision and under simulated deuteranopia, protanopia and tritanopia (Machado et al. 2009).
     - Set each threshold at today's value, so the palette can never get less distinguishable than it is now.
     - Every overlay has a legend word.
     - Record today's known collisions as known. Don't fix them here (`reference/meaning-contract.md`, "Known collisions").

   After this PR, the restyle PR changes none of these tests. If one has to change, that is a meaning change.
5. **Critique and audit.** Launch two agents in parallel: `templates/critique-a-app.md` (tasks and meaning) and `templates/critique-b-app.md` (tests, detector, accessibility, phone, performance and inventory). Merge their reports and store them with `critique-storage write`.
6. **Direction.**
   - Run `concept-seed --scope direction --mode persuade`. Ground the candidates in making maps: what the app does, told in physical things.
   - Exclude every sibling's world (below).
   - Say what each zone carries. The frame gets the world. The instruments borrow one or two disciplines from it, such as a numeral face or a rule. The map gets nothing.
   - **Choose an accent of the app's own.** Pine green is the hub's, and the current placeholder borrows it. The accent must:
     - hold 4.5:1 against white text;
     - stay far from the data palette (the water blues, badwater brown, the purples, dam orange and slope yellow);
     - stay far from the state colours.
   - Record the pick with `--kind assigned --from <key>`. Write `templates/direction-contract-app.md` and store it with `surface-brief write`.
   - If Kyler wants to choose, show him 2–3 candidates and wait.
7. **Build.** Work in this order:
   1. **Tokens.** Rename the current custom properties in `src/styles/app.css` and `editor.css` (`--bg`, `--panel`, `--accent`, `--bad`, `--ok`, `--warn` and the rest) to semantic tokens: surface, ink, muted, rule, accent, focus, and one per state (error, warning, advisory, ok). Grep every use.
   2. **Instruments.**
   3. **Frame.**
   4. **Phone layout.** PLAN §14.1: the generator page stacks, with settings in a drawer.

   While building, follow these rules:
   - **Fonts:** an OFL face that Google Fonts also serves. The website self-hosts it. The artifact edition fetches it at run time or inlines it (D41). Ship only the weights you use.
   - **Textures:** procedural, small, frame only, each with its provenance (`embed-prompt`). The artifact edition inlines them as `data:` URIs.
   - **Themes:** light and dark from the OS preference, with a toggle. Store the choice in `localStorage` under `damgoodmaps.theme`.
   - **Motion:** only what shows state, such as progress, a plan appearing, or the camera flying to an issue (EDITOR_PLAN §6). Under reduced motion, the camera jumps instead.
   - **Keyboard:** every tab, tool, report line and fix is reachable. The focus ring is visible over land, water and panels alike.
   - **Loading:** the 3D chunk stays lazy (PLAN §14.2).
8. **Verify once.** Run everything from step 2 again. These must match the baseline exactly:
   - every sha256;
   - the oracle, with 0 disagreements;
   - the benchmark budgets;
   - the step-4 guard tests, unchanged and green.

   Then check the new look:
   - **Captures:** capture the state matrix again, into `.scratch/captures/after/`.
   - **Meaning review:** go through every row of MEANING.md with the before and after captures side by side, and a greyscale copy of the after. Can each meaning still be read?
   - **Performance:** Lighthouse must be 90 or more on desktop (M13).
   - **Detector:** run `detect --json` on `src/styles` and on the built `dist/`. Triage the findings, and record lasting false positives in `.impeccable/config.json`.
   - **Artifact edition:** if it has been built, check its size and CSP with the spike checks. If not, confirm the design needs nothing the artifact can't load.

   Fix everything found in one batch.
9. **Finish review.** Use `impeccable:impeccable-finish-reviewer` with `templates/finish-review-app.md`, for at most 2 rounds. Round 2 goes to the same agent through SendMessage.
10. **Document.**
    - Run `impeccable:impeccable-documenter` to write DESIGN.md and `.impeccable/design.json`. DESIGN.md names the three zones and links MEANING.md.
    - Add an app section to the repo's CLAUDE.md, based on the site flow's `reference/claude-md-template.md`. It must include the order of authority, the hard limits, the zones, the meaning-change rule and the state-matrix command.
    - Add `.impeccable/.gitignore`, as the site flow does.
    - Log the pass in `docs/progress.md`, in the run's format.
11. **Ship.** Open a PR using `templates/pr-body-app.md`. When Kyler says merge: merge, deploy Pages from `main`, and check the live site.

## Update mode

For M12's Claude panels, M13's usability work, and any UI added later.

1. **Read the records:** CLAUDE.md, MEANING.md, DESIGN.md and the surface brief. Don't restyle; extend.
2. **Place every new element in a zone.** A new state gets its word in MEANING.md, a row in the state matrix and an ARIA snapshot, all in the same PR. New data colours go in `mapPalette.ts` and pass the palette test.
3. **Build from DESIGN.md's tokens and components.** If nothing fits, build the smallest new component and add it to DESIGN.md.
4. **Verify:** the full test suite, captures of the surfaces you touched, and the palette test.
5. **Review visual changes:** for a new component or a changed layout, do one finish-review round.
6. **Keep the records true:** MEANING.md, DESIGN.md and `design.json`.

## Ask Kyler

These are real product decisions. For anything else, decide, record it and keep going.

- Confirm MEANING.md, once.
- The direction, if he wants to pick it.
- Every meaning change.
- The editor on a phone. PLAN §14.1 covers only the generator page, and tablet and touch are under "Later" in the roadmap.
- Whether Dam Good Maps gets a panel on the hub, and in which group. The hub lists mods, and this is a tool.

## Sibling worlds to exclude

Each timbermods site has a world of its own. Dam Good Maps must not reuse any of them:
- Timber Together: River Station Signage.
- BeaverBuddies Stability Fork: blued steel and pine, the log round and saw.
- MixedStorage: a walnut apothecary drawer cabinet.
- Late Game Performance: Pit Crew.
- Optimized Local Housing: a banquet-hall seating plan.
- Hungry Pathing: enamel yard signs and a works canteen.
- Persistent Work Areas: a drafting plan with vellum overlays. A drafting plan or blueprint is the obvious look for a map tool, and this site already has it.
- The Tipsy Tail: a poolside bar.
- The hub: the lodge wall (walnut boards, brass nails, birch and forest floor).

`reference/timbermods-sites.md` in the site flow holds the current list.
