import unittest
from src.billing import generate_bill
from src.orders import orders
from src.menu import menu

class TestBilling(unittest.TestCase):

    def setUp(self):
        self.orders = [
            {"item_id": 1, "quantity": 2},  # Coffee
            {"item_id": 2, "quantity": 1},  # Tea
        ]
        self.expected_total = (menu[1]["price"] * 2) + (menu[2]["price"] * 1)

    def test_generate_bill(self):
        total = generate_bill(self.orders)
        self.assertEqual(total, self.expected_total)

    def test_empty_orders(self):
        total = generate_bill([])
        self.assertEqual(total, 0)

    def test_single_order(self):
        single_order = [{"item_id": 3, "quantity": 1}]  # Sandwich
        expected_total = menu[3]["price"]
        total = generate_bill(single_order)
        self.assertEqual(total, expected_total)

if __name__ == '__main__':
    unittest.main()