# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/aleens279-gif/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/aleens279-gif/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

The World in One Page — Tuesday 24 November 2026

Entry for make.fun's "Sum up 24 November's world news in one image" bounty.

## What it is

A newspaper front page (1024x1024 PNG) summing up Tuesday 24 November 2026:
a lead story, six more stories in a grid, and a footer strip of short items.
The page is drawn programmatically by `make-image.py` (Python + Pillow +
DejaVu fonts), so every word is spelled correctly and legible — no
AI-generated text.

## The day's stories

- **Lead — Technology:** Jensen Huang reinstated as Nvidia CEO after Trump
  intervened; his fortune jumps about $34 billion to $143.8 billion.
- **US:** Trump halts the planned detonation of explosives at an Iowa plant
  pending a court ruling, after the Army invoked emergency powers.
- **Asia:** A suspected North Korean aircraft breaches South Korea's airspace
  near Ulleung island; residents are ordered to shelters, and jets are
  scrambled as Russian warplanes enter the zone.
- **Ukraine war:** Leaked records put the Russian death toll in Ukraine near
  500,000; Moscow accuses Estonia of hostile actions "on the verge of
  triggering open war".
- **Climate:** The COP31 failure still reverberates; China calls the
  collapse disappointing.
- **Middle East:** Three tankers hit by sea mines catch fire in the Strait
  of Hormuz.
- **Tech:** US states sue Musk companies over sexualised images made with
  AI chatbot Grok.
- **Also today:** 2031 Women's World Cup hosts set; a 4.1 quake strikes
  Pakistan; the UN warns wars hit food aid for 7.3 million people; Honda
  recalls 810,000 vehicles.

## Run it

```sh
node main.ts   # writes /output/entry.png
```

`main.ts` copies the pre-rendered `entry.png` to `/output/entry.png`. It
takes no input and makes no network calls, so repeated runs produce
identical bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref=14mdadnq&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)</sub>
