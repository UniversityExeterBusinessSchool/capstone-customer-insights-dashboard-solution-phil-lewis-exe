import pytest
from src.analytics import total_spend_per_user, most_popular_product, churn_rate, average_order_value

def test_total_spend_per_user_basic():
    purchases = [
        {"username":"aisha","product_id":"P100","quantity":2},
        {"username":"aisha","product_id":"P300","quantity":1},
        {"username":"ben","product_id":"P200","quantity":1},
    ]
    prices = {"P100":12.99, "P200":19.99, "P300":29.50}
    out = total_spend_per_user(purchases, prices)
    assert out["aisha"] == pytest.approx(12.99*2 + 29.50, 0.01)
    assert out["ben"] == pytest.approx(19.99, 0.01)

def test_most_popular_product_tie_break():
    purchases = [
        {"username":"u1","product_id":"P1","quantity":2},
        {"username":"u2","product_id":"P2","quantity":2},
        {"username":"u3","product_id":"P1","quantity":1},
    ]
    pid, qty = most_popular_product(purchases)
    assert pid == "P1"
    assert qty == 3

def test_churn_rate_empty():
    assert churn_rate([]) == 0.0

def test_churn_rate_basic():
    users = [{"active": True}, {"active": False}, {"active": False}]
    assert churn_rate(users) == 66.67

def test_average_order_value_basic():
    purchases = [
        {"username":"a","product_id":"P1","quantity":2},
        {"username":"b","product_id":"P2","quantity":1},
        {"username":"c","product_id":"P1","quantity":1},
    ]
    prices = {"P1": 10.0, "P2": 5.0}
    assert average_order_value(purchases, prices) == pytest.approx(35/3, 0.01)
