from typing import Dict, List, Tuple
from collections import Counter

def total_spend_per_user(purchases: List[Dict], product_price_map: Dict[str, float]) -> Dict[str, float]:
    totals: Dict[str, float] = {}
    for row in purchases:
        price = product_price_map.get(row["product_id"], 0.0)
        qty = int(row.get("quantity", 0))
        totals[row["username"]] = round(totals.get(row["username"], 0.0) + price * qty, 2)
    return totals

def most_popular_product(purchases: List[Dict]) -> Tuple[str, int]:
    counter: Counter = Counter()
    for row in purchases:
        counter[row["product_id"]] += int(row.get("quantity", 0))
    if not counter:
        return ("", 0)
    pid, qty = counter.most_common(1)[0]
    return (pid, qty)

def churn_rate(customers: List[Dict]) -> float:
    if not customers:
        return 0.0
    inactive = sum(1 for u in customers if not bool(u.get("active", True)))
    return round(100 * inactive / len(customers), 2)

def average_order_value(purchases: List[Dict], product_price_map: Dict[str, float]) -> float:
    """Average spend per order (row): total revenue / number of rows.
    Returns 0.0 if no purchases.
    """
    if not purchases:
        return 0.0
    revenue = 0.0
    for r in purchases:
        price = product_price_map.get(r["product_id"], 0.0)
        qty = int(r.get("quantity", 0))
        revenue += price * qty
    return round(revenue / len(purchases), 2)
