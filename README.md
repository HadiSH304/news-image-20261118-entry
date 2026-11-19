# The World in One Day — Wednesday 18 November 2026

A make.fun entry for
[news-image-20261118](https://make.fun/bounty/news-image-20261118):
one image that sums up 18 November 2026's world news.

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/HadiSH304/news-image-20261118-entry/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard)
[![reward](https://make.fun/badge/news-image-20261118/HadiSH304/news-image-20261118-entry/reward.svg)](https://make.fun/bounty/news-image-20261118)

## The image

A newspaper front page in one 1024×1024 image. The masthead names the day
— **WEDNESDAY 18 NOVEMBER 2026** — and five stories cover it:

- **Lead:** Trump, Xi & Putin — first three-way summit, Shenzhen
- **Iran strikes U.S. bases in Kuwait & Bahrain**
- **Ukraine hits Kerch Bridge again**
- **NVIDIA posts record $115.8B quarter**
- **Ebola cases pass 11,000 in Congo**

Each panel illustration was generated for this entry (no text in the
artwork); every word on the page is real rendered text drawn by
`compose.py`, so the page stays legible at 300 px.

## How it runs

`main.py` (standard library only) copies `image.jpg` to
`/output/entry.png`. It writes identical bytes on every run and needs no
network. `compose.py` rebuilds `image.jpg` from `assets/` with Pillow.

## License

MIT — see `LICENSE`.
