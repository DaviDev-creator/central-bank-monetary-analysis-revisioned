# Central Bank Monetary Analysis (Automated)

## Overview
This skill is now powered by a Python engine that automates news gathering and data extraction for financial instruments.

## Execution
Run the automation script:
`python main.py <instrument> <date>`

## Technical Stack
- **Search**: Tavily API
- **Extraction**: Scrapegraphai
- **Data Mapping**: instruments.py
- **Fallback**: requests

## Data Structure
Mappping is handled in `instruments.py` via the `financial_instruments` dictionary.
