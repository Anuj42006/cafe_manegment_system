def generate_bill(orders, menu):
    if not orders:
        return "No orders to generate a bill."

    bill_lines = []
    total = 0
    for order in orders:
        item = menu[order["item_id"]]
        subtotal = item["price"] * order["quantity"]
        total += subtotal
        bill_lines.append(f"{item['name']} x {order['quantity']} = ${subtotal:.2f}")

    bill_output = "\n".join(bill_lines)
    bill_output += f"\nTotal: ${total:.2f}\nThank you for visiting!"
    
    return bill_output


def clear_orders(orders):
    orders.clear()