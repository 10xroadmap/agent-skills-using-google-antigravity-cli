---
name: fotd
description: Generate forecast of the day using age and gender
---
To forecast what will happen today you need age and gender of the person.
## Available scripts
- **`scripts/fotd.py`** — Generates forecast of the day suing gender and age as input parameters

Usage: scripts/fotd.py [OPTIONS] 

fotd input data and produce a summary report.

Options:
  --age age        input parameter age
  --gender gender  input parameter gender

Examples:
  scripts/fotd.py --age 23 --gender male

## Workflow
1. Run the script:
```bash
   python3 scripts/fotd.py 
```