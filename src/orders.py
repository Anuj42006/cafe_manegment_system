def take_order(menu, orders):
    display_menu(menu)
    try:
        item_id = int(input("Enter the item number to order: "))
        if item_id in menu:
            quantity = int(input("Enter quantity: "))
            orders.append({"item_id": item_id, "quantity": quantity})
            print(f"{menu[item_id]['name']} added to order.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def view_orders(orders, menu):
    if not orders:
        print("\nNo orders placed yet.")
        return

    print("\n--- Orders ---")
    total = 0
    for order in orders:
        item = menu[order["item_id"]]
        subtotal = item["price"] * order["quantity"]
        total += subtotal
        print(f"{item['name']} x {order['quantity']} = ${subtotal:.2f}")
    print(f"Total: ${total:.2f}")

def clear_orders(orders):
    orders.clear()