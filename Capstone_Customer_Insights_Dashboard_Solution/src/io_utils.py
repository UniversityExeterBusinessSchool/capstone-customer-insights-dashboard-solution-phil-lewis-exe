import csv, json
from typing import Dict, List

def load_customers_json(path: str) -> List[dict]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("users", [])
    except FileNotFoundError:
        print(f"[WARN] Customers file not found: {path}")
        return []
    except json.JSONDecodeError:
        print(f"[ERROR] Malformed JSON in: {path}")
        return []

def load_products_csv(path: str) -> Dict[str, dict]:
    products: Dict[str, dict] = {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            for i, row in enumerate(csv.DictReader(f), start=1):
                try:
                    row["price"] = float(row["price"])
                    products[row["product_id"]] = row
                except (KeyError, ValueError):
                    print(f"[WARN] Skipping bad product row {i}: {row}")
    except FileNotFoundError:
        print(f"[WARN] Products file not found: {path}")
    return products

def load_purchases_csv(path: str) -> List[dict]:
    rows: List[dict] = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for i, row in enumerate(csv.DictReader(f), start=1):
                try:
                    row["quantity"] = int(row["quantity"])
                    rows.append(row)
                except (KeyError, ValueError):
                    print(f"[WARN] Skipping bad purchase row {i}: {row}")
    except FileNotFoundError:
        print(f"[WARN] Purchases file not found: {path}")
    return rows
