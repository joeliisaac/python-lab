import unittest

from coffee_menu import CoffeeMenu

class TestBankAccount(unittest.TestCase):

    def setUp(self):
       self.menu = CoffeeMenu()

    def tearDown(self):
        self.menu = None

    def test_get_price_existing_item(self):
       self.assertEqual(self.menu.get_price('latte'), 2.75)
    
    def test_get_price_non_existing_item(self):
       with self.assertRaises(LookupError):
          self.menu.get_price('frappaccino')
       
    def test_add_item(self):
       updated_menu = {
        'espresso': 2.50,
        'latte': 2.75,
        'cappuccino': 3.20,
        'americano': 2.70,
        'frappe' : 4.32
        }
       self.menu.add_item('frappe', 4.32)
       self.assertEqual(self.menu.get_price('frappe'), 4.32)
       
       


if __name__ == '__main__':
  unittest.main()