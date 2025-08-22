# tools.py
import os

# Simulated orders data
orders = {
    "123": "Shipped",
    "456": "Processing",
    "789": "Delivered"
}

def get_order_status(order_id: str) -> str:
    """Return order status or error message."""
    if order_id in orders:
        return f"Order {order_id} is currently {orders[order_id]}."
    else:
        return "Sorry, we couldn't find that order ID. Please check and try again."
