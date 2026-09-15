# Hyderabad TDR Market Intelligence — Second Real Estate
Flagship Final Stable — GitHub Push Ready — Build f1a93a2917b7

Swiss editorial #FFFEFB #111113 #6B7280 #0A84FF — 11 sections flow locked — 82vh MapLibre real accurate map — Deterministic NO Math.random()

## What this is
Hyderabad's Second Real Estate = Transferable Development Rights (TDR) — unused building rights that can be bought & sold, like air rights.

This is the flagship final stable build with time machine fixed:
- **Cumulative dots:** 1 / 17 / 27 / 47 / 76 / 111 / 159 / 196 / 240
- **RERA mapping:** 66 / 747 / 483 / 914 / 1337 / 1613 / 2254 / 1724 / 2072 = 11,210 total
- **Animation:** 1500ms per year = 12s total 2018 oldest (1 dot) → 2026 recent (240 dots) — smooth, no same-dots blinking, different dots per year
- **Map:** 82vh real MapLibre — OpenFreeMap Positron tiles https://tiles.openfreemap.org/styles/positron — Carto fallback — Offline canvas fallback deterministic — Accurate verified centroids Agent 4
- **Stack:** Single index.html, no build step, truly offline, system fonts, deterministic offsets, no Math.random()

## Data
- TDR: 2,092 accounts, GHMC portal Sept 12 2026, cleaner.py→geocoder.py→mapper.py→aggregator.py, 1,298 / 2,092 geocoded 62%
- RERA: 11,210 projects canonical
- Market size: Initial 56.55L, Utilized 42.86L 75.8%, Available 10.92L 19.3%, In-progress 2.77L
- Spatial: Moran I 0.22 Expected -0.00077 SD 0.031 z 7.1 p<0.001 permutation 999 KNN k=8
- Concentration: Cert HHI 0.068 Top1 22.7% Top5 45% — Zone HHI 0.24 — Largest 247,779.32 SQYD @4400

## Sections (11)
1. Hero — 2,092 / 10.92L / 42.86L / 11,210
2. Observed vs Derived vs Modeled
3. Market in one view — 5 findings
4. Market size + Sankey 56.55L→42.86L+10.92L
5. Spatial market map — 82vh visual centerpiece — Time machine 2018→2026 — TDR Sourcing Mode
6. Market archetypes + Ownership — Top10 holders
7. Market activity + TDR×RERA — Lead/lag +2y r=0.42 association not causation
8. Spatial econometrics + regression lab — R² 0.143 exploratory
9. Development capacity lab — BUA TDR=BUA/9 YoC IRR DSCR
10. 60 scenarios — 21.10L MODELED BUA — deterministic NO Math.random()
11. So what? + Evidence — Provenance — Data quality 52 tests — Limitations

## Quick start
`index.html` is the entire app. Just open it.
```
open index.html
# or
python3 -m http.server 8000
```

## GitHub Pages
This repo is Pages-ready. Push to `main`, enable Pages → Source: GitHub Actions.
Workflow: `.github/workflows/pages.yml` uploads artifact and deploys.

No API keys. Tiles from OpenFreeMap (weekly OSM planet) — No limits. Attribution: © OpenFreeMap © OpenMapTiles © OpenStreetMap contributors.

## Build info
- Build: f1a93a2917b7
- Time machine: Fixed dots — buildAllFeatures = ALL 240 + setFilter issue_year — no same dots blinking
- Year ladder: explicit if idx<1 2018, <17 2019, <27 2020, <47 2021, <76 2022, <111 2023, <159 2024, <196 2025 else 2026
- Colors: Swiss #FFFEFB bg #111113 text #6B7280 muted #0A84FF accent

## Provenance
GHMC TDR Portal extracted Sept 12 2026 — OSM Nominatim bounded=1 city-scoped near (17.3850,78.4867) — TSRERA 11,210 — Agent 4 verified Hyderabad centroids.

© OpenStreetMap contributors ODbL — MapLibre BSD — OpenFreeMap — CARTO — Second Real Estate Data edition Sept 2026
