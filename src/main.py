import sys
import json
from menu import load_menu, display_menu
from orders import take_order, view_orders
from billing import generate_bill

def main():
    menu = load_menu()
    orders = []

    while True:
        print("\n--- Café Management System ---")
        print("1. Display Menu")
        print("2. Take Order")
        print("3. View Orders")
        print("4. Generate Bill")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                display_menu(menu)
            elif choice == 2:
                order = take_order(menu)
                if order:
                    orders.append(order)
            elif choice == 3:
                view_orders(orders, menu)
            elif choice == 4:
                generate_bill(orders, menu)
                orders.clear()
            elif choice == 5:
                print("Exiting the system. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()