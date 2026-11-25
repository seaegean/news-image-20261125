# The Daily Ledger — Wednesday 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/seaegean/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/seaegean/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A make.fun news-image entry: one image summing up the world news of
Wednesday 25 November 2026, in the style of a classic newspaper front
page.

Bounty: https://make.fun/bounty/news-image-20261125
Referral code: `cqypmhf6`

## The front page

**Lead — "TANKERS ABLAZE AFTER MINES STRIKE IN THE STRAIT":**
Iran's Revolutionary Guard says at least two oil tankers exploded and
caught fire after striking naval mines while transiting what the Guard
called an unauthorised route through the Strait of Hormuz, according to
Iranian state media early on Wednesday. A further tanker was later
reported on fire east of the strait, and a container ship carrying more
than 2,500 containers sank south of the strait after hitting a mine on
Tuesday. Iran says the strait is closed and under its control amid the
war with the United States; the Guard says it downed two US drones over
the strait overnight, and the US is investigating Iran as a suspect in
cyberattacks on up to 50 energy tankers.

**Middle East — "U.S. WARNS CITIZENS IN MIDDLE EAST":** Washington
warned Americans in the region of an increased threat from Iran-backed
Houthis. Secretary of State Marco Rubio condemned Houthi attacks in a
call with the Saudi foreign minister.

**Space — "SHENZHOU-24 LIFTS OFF WITH FIRST FOREIGN ASTRONAUT":**
China launched Shenzhou-24 carrying a Pakistani national, the first
foreign astronaut on China's space station.

**Business — "SHEIN TO PAY $100M IN U.S. SETTLEMENT":** Shein will pay
$100 million to settle US trade allegations over deceptive practices.

**US — "SIX FEARED MISSING AFTER PLANE CRASH OFF MISSISSIPPI":** Six
people are feared missing after a plane crashed off Horn Island; the US
Coast Guard is searching.

**Markets — "MARKETS SLIDE AS INVESTORS WEIGH HUANG'S RETURN":** The
Nasdaq and the S&P 500 ended lower as investors assessed Jensen Huang's
return to Nvidia. Huang apologised to staff and says he is in "therapy".
The slide is charted on the page.

**In brief:** Gaza — Israeli airstrikes killed seven, including
Hamas's internal security director Naim Abu Nahal, despite the
ceasefire. A wrongly deported Salvadoran man is voluntarily leaving the
US, a US senator says. Huawei was found guilty on 10 of 12 counts on
TUESDAY; the company says it will appeal. COP31 ended without a deal on
SUNDAY 22 Nov. Iraq seeks a higher oil output capacity estimate ahead
of the 2027 OPEC+ quota debate.

## Accuracy notes

- The Hormuz mine story is framed throughout as an IRGC claim, never
  as verified fact: the page says the Guard "says" tankers hit mines,
  and the dek states plainly that the claim has not been independently
  verified.
- No firm tanker total is given anywhere on the page. Counts varied
  across IRGC statements (two, then three, then four), so the page says
  "tankers" / "at least two" only.
- Every claim is attributed where it is a claim ("Iran's Revolutionary
  Guard says", "reports say", "the US says", "a US senator says").
- No Article 4 / Article 5 language appears anywhere on the page.
- The Huawei verdict (Tuesday 24 Nov) and the COP31 outcome (Sunday
  22 Nov) are dated and kept to the briefs strip — neither leads, and
  neither is presented as 25 November news.
- The strait illustration is a drawn illustration, labelled as such on
  the page — not a photograph.
- Date on the page: WEDNESDAY 25 NOVEMBER 2026.

## The image

`entry.png` — "The Daily Ledger" classic newspaper front page,
grayscale, 1024×1024, drawn programmatically with Python/PIL.

- Size: 70,452 bytes (under the 1 MiB limit)
- Dimensions: 1024 × 1024
- SHA-256: `a4e4a1d5f03c61abdb3567b4535de4141799019af6db884f7d50eb11259b4347`

## Run

`main.py` is a deterministic, stdlib-only program (Python 3.12+, no
network). It verifies `entry.png` — PNG signature, 1024×1024 IHDR,
8-bit grayscale, IEND trailer, size under 1 MiB, and SHA-256 against
the hash recorded in the program — then writes an identical copy to
the output directory (default `/output/entry.png`).

```sh
python3 main.py                 # writes to /output/entry.png
python3 main.py ./output        # writes to ./output/entry.png
```

Run twice and the two outputs are byte-identical to `entry.png`
(verified with `cmp` and matching SHA-256 hashes).

## License

MIT — see [LICENSE](LICENSE).
