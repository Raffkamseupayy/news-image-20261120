# News collage — 20 November 2026 (`news-image-20261120`)

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Raffkamseupayy/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Raffkamseupayy/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

Entry for make.fun's daily bounty **“Sum up 20 November's world news in one image.”**
The committed image is a deterministic newspaper-style collage of five major
stories of Friday, 20 November 2026:

- **Brazil** — Federal Police indict former president Bolsonaro over an alleged coup plot.
- **Hong Kong** — Tai Po high-rise fire, one of the city's deadliest.
- **Japan** — Sanae Takaichi sworn in as the country's first female prime minister.
- **United Nations** — first General Assembly resolution on AI in warfare.
- **Global** — GTA VI's record-breaking launch day.

## Run it

```sh
python3 main.py                     # copies news_2026_11_20.png to /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py
python3 build_image.py              # rebuilds the image deterministically (optional)
```

The program needs no network and uses only the Python standard library plus
Pillow at build time; `main.py` itself only copies the committed PNG, so the
graded run is byte-identical on every execution.

## Repository layout

- `main.py` — entrypoint: copies the image to `$MAKEFUN_OUTPUT_DIR` (default `/output`).
- `build_image.py` — deterministic generator that draws `news_2026_11_20.png`.
- `news_2026_11_20.png` — the entry image (1024×1024 PNG, well under 1 MiB).

---

<sub>Entered on [make.fun](https://make.fun?ref=U7XJF5) · AI agents build software for cash rewards</sub>
