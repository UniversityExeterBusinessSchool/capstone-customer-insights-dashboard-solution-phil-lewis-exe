from pathlib import Path
import json
import matplotlib.pyplot as plt

from src.io_utils import load_customers_json, load_products_csv, load_purchases_csv
from src.analytics import total_spend_per_user, most_popular_product, churn_rate, average_order_value

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
OUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
OUT_DIR.mkdir(exist_ok=True)

def compute_summary():
    customers = load_customers_json(str(DATA_DIR / "customers.json"))
    products = load_products_csv(str(DATA_DIR / "products.csv"))
    purchases = load_purchases_csv(str(DATA_DIR / "purchases.csv"))
    price_map = {pid: float(info["price"]) for pid, info in products.items()}

    spend = total_spend_per_user(purchases, price_map)
    popular_pid, popular_qty = most_popular_product(purchases)
    churn = churn_rate(customers)
    aov = average_order_value(purchases, price_map)

    summary = {
        "spend_by_user": spend,
        "most_popular": {"product_id": popular_pid, "qty": popular_qty},
        "churn_rate_pct": churn,
        "average_order_value": aov,
    }
    with open(OUT_DIR / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    return summary

def plot_spend_by_user(spend_by_user: dict, save: bool = True):
    users = list(spend_by_user.keys())
    totals = [spend_by_user[u] for u in users]
    plt.figure()
    plt.bar(users, totals)
    plt.title("Total Spend by User (£)")
    plt.xlabel("User")
    plt.ylabel("Spend (£)")
    for i, v in enumerate(totals):
        plt.text(i, v + 0.2, f"{v:.2f}", ha="center")
    plt.tight_layout()
    if save:
        plt.savefig(OUT_DIR / "spend_by_user.png", dpi=150)
    plt.show()

def plot_popular_product(popular: dict, save: bool = True):
    pid = popular.get("product_id", "")
    qty = popular.get("qty", 0)
    plt.figure()
    plt.bar([pid], [qty])
    plt.title("Most Popular Product (by quantity)")
    plt.xlabel("Product ID")
    plt.ylabel("Quantity")
    plt.tight_layout()
    if save:
        plt.savefig(OUT_DIR / "most_popular_product.png", dpi=150)
    plt.show()

def plot_churn(churn_rate_pct: float, save: bool = True):
    plt.figure()
    plt.bar(["Active","Churned"], [100 - churn_rate_pct, churn_rate_pct])
    plt.title("Churn Rate (%)")
    plt.ylabel("Percentage")
    vals = [100 - churn_rate_pct, churn_rate_pct]
    for i, v in enumerate(vals):
        plt.text(i, v + 0.2, f"{v:.2f}%", ha="center")
    plt.tight_layout()
    if save:
        plt.savefig(OUT_DIR / "churn_rate.png", dpi=150)
    plt.show()

def plot_aov(aov: float, save: bool = True):
    plt.figure()
    plt.bar(["Average Order Value"], [aov])
    plt.title("Average Order Value (£)")
    plt.ylabel("£")
    plt.text(0, aov + 0.2, f"{aov:.2f}", ha="center")
    plt.tight_layout()
    if save:
        plt.savefig(OUT_DIR / "average_order_value.png", dpi=150)
    plt.show()

def main_menu():
    summary = compute_summary()
    while True:
        print("\n=== Customer Insights Dashboard (Solution) ===")
        print("[1] View spend by user (bar)")
        print("[2] View most popular product (bar)")
        print("[3] View churn rate (bar)")
        print("[4] View average order value (bar)")
        print("[5] Recompute summary")
        print("[0] Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            plot_spend_by_user(summary["spend_by_user"])
        elif choice == "2":
            plot_popular_product(summary["most_popular"])
        elif choice == "3":
            plot_churn(summary["churn_rate_pct"])
        elif choice == "4":
            plot_aov(summary["average_order_value"])
        elif choice == "5":
            summary = compute_summary()
            print("Summary recomputed and saved to outputs/summary.json")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Please choose a valid option.")

if __name__ == "__main__":
    main_menu()
