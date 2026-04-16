---
name: central-bank-monetary-analysis
description: Use when monitoring global interest rates, extracting policy data from central bank portals, or projecting future monetary scenarios based on official bank guidance.
---

# Collegamento Principale: Central Bank Analysis

## Overview
This skill provides a standardized process for extracting monetary policy data from the world's leading central banks and synthesizing this data into forward-looking economic scenarios.

## When to Use
Use this skill when you need to:
- Update a global interest rate dashboard.
- Analyze divergence in monetary policy across different regions.
- Project future rate paths based on official forward guidance.
- Extract a "snapshot" of current policy rates and decisions.

## Core Pattern
The process follows a three-step cycle: **Extract $\rightarrow$ Compare $\rightarrow$ Project**.

### 1. Extraction (The "Collegamento")
Access the following official portals to extract: **Current Policy Rate**, **Recent Decision**, and **Forward Guidance**.

| Central Bank | Official URL |
| :--- | :--- |
| Federal Reserve | https://www.federalreserve.gov |
| ECB | https://www.ecb.europa.eu |
| Bank of England | https://www.bankofengland.co.uk |
| Bank of Japan | https://www.boj.or.jp/en |
| SNB | https://www.snb.ch/en |
| Bank of Canada | https://www.bankofcanada.ca |
| RBA | https://www.rba.gov.au |
| RBNZ | https://www.rbnz.govt.nz |
| Norges Bank | https://www.norges-bank.no/en |
| Riksbank | https://www.riksbank.se/en-gb |

### 2. Comparison
Organize the extracted data into a structured table to identify trends:
- **Hawkish**: Signaling hikes or maintaining high rates despite growth slow-down.
- **Dovish**: Signaling cuts or prioritizing growth/inflation targets.
- **Neutral**: Holding steady with data-dependent guidance.

### 3. Projection (Future Scenarios)
Synthesize the findings into a projected scenario for the next quarter. The projection must include:
- **The Primary Narrative**: (e.g., "Vigilant Pause", "Synchronized Easing").
- **Divergence Analysis**: Identify which banks are moving away from the global trend.
- **Risk Factors**: List geopolitical or economic triggers that could change the projection.

## Implementation Example
**Request:** "Analyze current rates and project Q3."

**Action:**
1. Visit the 10 URLs listed above.
2. Extract rates (e.g., Fed 3.5%, ECB 2.0%).
3. Build the Comparison Table.
4. Write the Projection: "I project a 'Fragmented Volatility' scenario where Norges Bank hikes while the Fed remains on hold due to [extracted risk factor]."

## Common Mistakes
- **Relying on general knowledge**: ALWAYS visit the URLs for the most recent meeting minutes/decisions.
- **Omitting forward guidance**: The rate is the "what"; the guidance is the "why" and "what next."
- **Generic projections**: Avoid "rates might change." Use specific terminology (e.g., "divergence," "pivot," "plateau").
