# Capstone Project: Customer Insights Dashboard — **Solution**

This folder contains a **reference implementation** of the dashboard capstone for Weeks 9–10.

## What’s included
- Fully implemented analytics functions (including `average_order_value`).
- A working dashboard script (`src/dashboard.py`) that:
  - Computes summary metrics
  - Generates bar charts with Matplotlib
  - Saves outputs (.png) into `outputs/` and JSON summary to `outputs/summary.json`
- Pytest test suite with all tests **passing**.

## How to run
```bash
pip install -r requirements.txt
pytest -q
python -m src.dashboard
```

## Notes
- Charts avoid custom styles and use **Matplotlib only**.
- Each figure uses a single chart (no subplots).
- Colours are left to Matplotlib defaults.
