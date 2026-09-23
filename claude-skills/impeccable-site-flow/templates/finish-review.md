Finish review (round 1 of at most 2) of the redesigned <site name> website.

Project root: <path>. The site is in <dir>: <pages, with the mode of each (Persuade or Read)>. Served at <local URL>. If the 404 uses absolute paths, it only styles correctly on Pages, so judge it from source. Styles: <css>. Scripts: <js and what each does>. <release.js is shared and byte-identical: never suggest editing it.>

Direction contract: .impeccable/surfaces/<brief>.md ("<direction name>", seed <key>). Product context: PRODUCT.md, including its standing rules: honest status, no version history on player pages, no invented numbers, no Timberborn art, both themes, all ids kept. Critique snapshot: .impeccable/critique/. There is no approved comp, so judge the build against the contract and the chosen world's quality bar.

Captures are from Playwright on Edge, with reduced motion and all images loaded, in <caps dir>:
- desktop.png and desktop-dark.png (1440 wide);
- mobile.png and mobile-dark.png (a true 390px phone);
- a -top.png crop of each;
- <page>-desktop.png for the other pages (first viewport).

There is no horizontal overflow. The pages are tall, so crop them with Python/Pillow as needed.

Build notes:
- <deliberate deviations from the contract, and why>
- <detector leftovers triaged as false positives, and why>
- <content fixes made (copy, status, links)>
- <hard constraints the reviewer must respect (test hooks, bot-generated files)>

Return an ordered list of material fixes, most important first, each with the file or selector and the concrete change. End with a verdict: ship or fix.
