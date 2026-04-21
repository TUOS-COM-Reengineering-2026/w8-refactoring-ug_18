import unittest
import io
import contextlib

from main import CustomerManager

class TestCustomerManager(unittest.TestCase):

    def test_add_customer(self):
        cm = CustomerManager()
        name = "Alice"
        purchases = [{'price': 50, 'item': 'banana'}, {'price': 80, 'item': 'apple'}]
        cm.add_customer(name, purchases)

        self.assertEqual(
            {name: purchases},
            cm.customers
        )

    def test_add_purchase(self):
        cm = CustomerManager()
        name = "Alice"
        purchase = {'price': 50, 'item': 'banana'}
        cm.add_purchase(name, purchase)

        self.assertEqual(
            {name: [purchase]},
            cm.customers
        )

    def test_add_purchase_multiple(self):
        cm = CustomerManager()
        name = "Alice"
        purchase = {'price': 50, 'item': 'banana'}
        cm.add_purchase(name, purchase)
        cm.add_purchase(name, purchase)

        self.assertEqual(
            {name: [purchase, purchase]},
            cm.customers
        )

    def test_discount_eligibility(self):
        cm = CustomerManager()
        cm.add_customer("Bob", [{'price': 600}])

        # Capture printed output
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            cm.generate_report()

        output = captured.getvalue()

        self.assertIn("Bob", output)
        self.assertIn("Eligible for discount", output)

    def test_heavy_item_shipping_fee(self):
        cm = CustomerManager()
        purchases = [{'price': 100, 'weight': 25}]

        fee = cm.calculate_shipping_fee_for_heavy_items(purchases)
        self.assertEqual(fee, 50)

    def test_fragile_item_shipping_fee(self):
        cm = CustomerManager()
        purchases = [{'price': 70, 'fragile': True}]

        fee = cm.calculate_shipping_fee_for_fragile_items(purchases)
        self.assertEqual(fee, 60)

    def test_no_special_items_shipping_fee(self):
        cm = CustomerManager()
        purchases = [{'price': 40, 'weight': 5, 'fragile': False}]

        fee = cm.calculate_shipping_fee_for_heavy_items(purchases)
        self.assertEqual(fee, 20)

        fee_fragile = cm.calculate_shipping_fee_for_fragile_items(purchases)
        self.assertEqual(fee_fragile, 25)
        
    def test_add_purchases(self):
        cm = CustomerManager()
        name = "Alice"
        purchases = [{'price': 50, 'item': 'banana'}, {'price': 80, 'item': 'apple'}]
        
        cm.add_purchases(name, purchases)
        
        self.assertEqual(
            {name: purchases},
            cm.customers
        )
        
    def test_calculate_shipping_fee_for_heavy_items_20(self):
        cm = CustomerManager()
        purchases = [{'price': 50, 'item': 'banana'}, {'price': 80, 'item': 'apple'}]
        
        fee = cm.calculate_shipping_fee_for_heavy_items(purchases)
        self.assertEqual(fee, 20)
        
    def test_calculate_shipping_fee_for_heavy_items_50(self):
        cm = CustomerManager()
        purchases = [{'price': 50, 'item': 'banana', 'weight': 100}, {'price': 80, 'item': 'apple', 'weight': 100}]
        
        fee = cm.calculate_shipping_fee_for_heavy_items(purchases)
        self.assertEqual(fee, 50)  

    def test_generate_report_lt_tax_threshold(self):
        cm = CustomerManager()
        cm.add_customer("Bob", [{'price': 10}])

        # Capture printed output
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            cm.generate_report()

        captured.getvalue()
        
    def test_generate_report_potential_future_customer(self):
        cm = CustomerManager()
        cm.add_customer("Bob", [{'price': 301}])

        # Capture printed output
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            cm.generate_report()

        captured.getvalue()
        
    def test_generate_report_vip_customer(self):
        cm = CustomerManager()
        cm.add_customer("Bob", [{'price': 1001}])

        # Capture printed output
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            cm.generate_report()

        captured.getvalue()
        
    def test_generate_report_priority_customer(self):
        cm = CustomerManager()
        cm.add_customer("Bob", [{'price': 801}])

        # Capture printed output
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            cm.generate_report()

        captured.getvalue()
    
if __name__ == "__main__":
    unittest.main()
