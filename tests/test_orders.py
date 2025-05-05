import unittest
from src.orders import take_order, view_orders, orders
from src.menu import menu

class TestOrderManagement(unittest.TestCase):

    def setUp(self):
        orders.clear()  # Clear orders before each test

    def test_take_order_valid(self):
        take_order(item_id=1, quantity=2)  # Simulate taking an order
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0]['item_id'], 1)
        self.assertEqual(orders[0]['quantity'], 2)

    def test_take_order_invalid_item(self):
        initial_order_count = len(orders)
        take_order(item_id=99, quantity=1)  # Invalid item ID
        self.assertEqual(len(orders), initial_order_count)  # No new order should be added

    def test_take_order_invalid_quantity(self):
        initial_order_count = len(orders)
        take_order(item_id=1, quantity=-1)  # Invalid quantity
        self.assertEqual(len(orders), initial_order_count)  # No new order should be added

    def test_view_orders_empty(self):
        self.assertEqual(view_orders(), "No orders placed yet.")

    def test_view_orders_with_orders(self):
        take_order(item_id=1, quantity=2)
        output = view_orders()
        self.assertIn("Coffee x 2", output)  # Check if the order is displayed

if __name__ == '__main__':
    unittest.main()