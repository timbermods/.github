Finish review (round 1 of at most 2) of Dam Good Maps' design pass.

Project root: <path>. Served at <local URL> (`vite preview` of a fresh build).
- Styles: <files>.
- UI: `src/ui`, `src/editor`.
- Map rendering: `src/ui/Preview2D.tsx`, `src/render3d`, and `src/ui/mapPalette.ts`. These are zone M: never suggest styling them.

Records:
- the direction contract: .impeccable/surfaces/<brief>.md ("<direction name>", seed <key>);
- MEANING.md: what must still read;
- PRODUCT.md;
- the critique snapshot in .impeccable/critique/.

There is no approved comp, so judge the build against the contract, MEANING.md and the chosen world's quality bar.

Captures come from `tools/capture-states.ts`, with reduced motion:
- before: <scratch>/captures/before/;
- after: <scratch>/captures/after/.

Each state comes as desktop and phone, in light and dark, with a greyscale copy. `index.md` pairs each file with its meaning.

Judge in this order:
1. **Meaning (blocking).** Go through every row of MEANING.md in the after captures, and again in greyscale. Is each meaning still legible? These are P0:
   - a meaning that is weaker than before;
   - a state shown by colour alone;
   - any meaning change missing from the PR's Meaning changes table.
2. **Zones.** Texture, gradient, glow or theme colour on the map, or behind numbers or report text, is P0. The instruments should be calm and dense. The world should live in the frame.
3. **Craft.** Read <IMP>/reference/craft-floor.md and polish.md. Judge type, spacing, alignment, both themes and the phone layout.
4. **Accessibility.** Contrast; the focus ring over the map; targets (44px in the frame and on phones, at least 24px in desktop instruments); live regions; reduced motion.
5. **Contract.** The guard tests are unchanged, and every sha256 is equal. List anything that suggests otherwise.

Build notes:
- <deliberate deviations from the contract, and why>
- <detector leftovers triaged as false positives, and why>
- <meaning changes proposed, with their status>
- <hard constraints: `shade.ts` is pinned, `src/core` is untouched, and the test hooks stay>

Return an ordered list of material fixes, most important first, each with the file or selector and the concrete change. End with a verdict: ship or fix.
