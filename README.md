[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Plowester1/news-image-20261119-poler-v1/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Plowester1/news-image-20261119-poler-v1/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# The World in One Day — 19 November 2026

An entry in make.fun's **"Sum up 19 November's world news in one image"**
bounty (news-image-20261119, FREE entry, $250 pot). The program copies a
single 1024×1024 infographic to `/output/entry.png`: a light newspaper
front page summing up Thursday 19 November 2026's world news in twenty-two
stories, each verified against multiple news sources for that day.

## The twenty-two stories

1. **Diplomacy** — Trump, Xi and Putin meet in Shenzhen: trilateral talks on
   nuclear arms and the Ukraine and Iran wars; APEC opens, Trump already met
   Xi and Putin separately.
2. **N. Korea** — IAEA: N. Korea expanding enrichment: Yongbyon extension
   finished Oct.
3. **Justice** — World Court rules on Rohingya genocide: ICJ judgment in
   Gambia v. Myanmar.
4. **Bangladesh** — Yunus's ancestral home set ablaze: amid Awami League
   protests.
5. **Ukraine** — Russian strike on Odesa kills 4: 13 wounded; figures
   unconfirmed.
6. **Crimea** — Ukraine hits Kerch Bridge again: rail traffic disrupted.
7. **Europe** — EU proposes €45bn loan to Ukraine: to sustain support for
   Kyiv.
8. **Cyber** — Cyberattack hits European Commission: extent and culprit
   unknown.
9. **Culture** — Van Gogh sells for record $190.4M: Nazi-era ownership row.
10. **Energy** — Three tankers ablaze in Hormuz: IEA warns on energy
    security.
11. **Middle East** — Houthi missile intercepted over Riyadh: missile
    downed, launcher hit.
12. **Gaza** — Israel strikes Nuseirat in Gaza: homes destroyed; ceasefire
    claims.
13. **Tech** — Trump slams 'globalist' AI rules: chip and data rivalry heats
    up.
14. **US Politics** — Musk regrets midterm spending: reflects on 2026
    campaign outlays.
15. **Venezuela** — US, Venezuela restore military ties: Hegseth announces
    deal in Caracas.
16. **Haiti** — Pastor convicted in Moïse killing: Miami verdict on 2021
    killing.
17. **Health** — Ebola fight hampered in DR Congo: insecurity slows the
    response.
18. **Sudan** — RSF commander defects to army: defection adds to war
    uncertainty.
19. **Migration** — Dozens missing as boat sinks: migrant vessel off
    Senegal, ~100 aboard.
20. **Pacific** — Fiji declares drought disaster: El Niño threatens water
    supplies.
21. **Weather** — 72,000 evacuated for Cyclone Akvan: storm nears Andhra
    Pradesh coast.
22. **Diplomacy** — Xi pushes APEC trade integration and tech cooperation:
    extra funding for digital tech, clean energy and smaller businesses.

## How it is built

`entry.png` is composed programmatically with Python PIL (`build_image.py`):
crisp vector text, a light newspaper front-page layout with a full-width
hero lead, color-coded story cards and drawn icon motifs, no AI-generated
imagery, so every headline is legible and correct. `main.py` is a pure
file copy — no network, no randomness — so both runs write identical bytes,
verified with a SHA-256 output-vs-source check.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# out/entry.png — 1024x1024 PNG, identical on every run
```
