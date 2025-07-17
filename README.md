## Where the Trees Fall: Macroeconomic Forecasts for Forest Reliant States

>Note: This repository corresponds to the pre-print: https://arxiv.org/abs/2503.23569

### Files and Processing
1. **Stata `.do` files** — Run models for each state and sector
2. **Stata `.dta` files** — Contain the underlying data per sector (NAICS 113, 321, 322)
3. **Python Script: `KEYStateGraphs.py`** — Graphs forecast results by sector

> There are:
> - 3 Python and 3 `.dta` files (one per industry)
> - 16 `.do` files: 5 states for NAICS 113, 6 for NAICS 321, and 5 for NAICS 322

### Stata `.do` File Workflow
Each `.do` file:
- Imports sector-specific `.dta` data
- Tests for lag length and cointegration rank
- Runs VEC model
- Generates 5-year forecasts
- Conducts robustness checks
- Exports final forecasts

### Python Script Workflow
- Imports the forecast data
- Visualizes each state's forecasts across the three industries
