Record DESIGN.md and its sidecar (.impeccable/design.json) for the finished <site name> website redesign, derived from the shipped files.

Project root: <path>. Site: <dir>. It contains:
- pages: <list>;
- styles: <css>;
- scripts: <js, and what each does>;
- <release.js: shared and byte-identical, so not part of the design system>;
- fonts: <fonts and weights (OFL)>;
- textures: <files, made by make_textures.py, with provenance sidecars>;
- <favicon>.

Direction contract: .impeccable/surfaces/<brief>.md ("<direction name>"). Product context: PRODUCT.md. <Neither DESIGN.md nor design.json exists yet, so write both new. | Replace the old ones.> Served locally at <URL>.

The finish review closed with: <a summary of what the build ended up being: the signature device, how colour is reserved, the themes, the phone layout>.

Record what is actually built: tokens for both themes, type, components, layout, motion, and the named rules and don'ts. Note any drift you see between the contract and the build, but edit no files other than DESIGN.md and .impeccable/design.json. Report leftovers and defects rather than canonizing them.
