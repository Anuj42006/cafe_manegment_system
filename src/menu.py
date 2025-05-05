import json
import os

menu_file_path = os.path.join(os.path.dirname(__file__), '../data/menu.json')

def load_menu():
    if not os.path.exists(menu_file_path):
        return {}
    
    with open(menu_file_path, 'r') as file:
        return json.load(file)

def display_menu(menu):
    print("\n--- Menu ---")
    for item_id, item_info in menu.items():
        print(f"{item_id}. {item_info['name']} - ${item_info['price']:.2f}")
    print()

def add_menu_item(name, price):
    menu = load_menu()
    new_id = max(menu.keys(), default=0) + 1
    menu[new_id] = {"name": name, "price": price}
    save_menu(menu)

def update_menu_item(item_id, name=None, price=None):
    menu = load_menu()
    if item_id in menu:
        if name is not None:
            menu[item_id]['name'] = name
        if price is not None:
            menu[item_id]['price'] = price
        save_menu(menu)
    else:
        print("Item ID not found in the menu.")

def save_menu(menu):
    with open(menu_file_path, 'w') as file:
        json.dump(menu, file, indent=4)