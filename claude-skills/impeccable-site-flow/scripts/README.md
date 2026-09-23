# Scripts

- `capsite.py <base-url> <out-dir> "" page2.html ...`: full-page review captures (desktop and phone, light and dark)
  using Playwright on the installed Edge. Needs `pip install playwright pillow`. There's no need to run
  `playwright install`, because it drives the installed Microsoft Edge.
- `make_textures_example.py`: the hub's procedural texture generator (felt, PVC binder, sleeve sheen). Copy the
  pattern: numpy and Pillow, fixed seeds, tileable wrap noise, and one output per theme. Put the script beside its
  outputs and run it from that folder.
