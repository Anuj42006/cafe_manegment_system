import unittest
from src.menu import load_menu, display_menu, add_menu_item, update_menu_item

class TestMenu(unittest.TestCase):

    def setUp(self):
        self.menu = load_menu()

    def test_load_menu(self):
        self.assertIsInstance(self.menu, dict)
        self.assertGreater(len(self.menu), 0)

    def test_display_menu(self):
        with self.assertLogs(level='INFO') as log:
            display_menu()
            self.assertIn('Menu:', log.output[0])

    def test_add_menu_item(self):
        new_item = {"name": "Pastry", "price": 2.50}
        add_menu_item(new_item)
        self.assertIn(new_item['name'], self.menu)

    def test_update_menu_item(self):
        updated_item = {"name": "Coffee", "price": 6.00}
        update_menu_item(updated_item)
        self.assertEqual(self.menu[1]['price'], 6.00)

if __name__ == '__main__':
    unittest.main()