from typing import Dict, List, TypedDict

class Purchase(TypedDict):
    price: float
    item: str

class CustomerManager:
    def __init__(self):
        self.customers: Dict[str, List[Purchase]] = {}
        self.tax_rate = 0.2
        self.tax_threshold = 100
        self.discount_threshold = 500

    def add_customer(self, name: str, purchases: List[Purchase]):
        if name in self.customers.keys():
            self.customers[name].extend(purchases)
        else:
            self.customers[name] = purchases

    def add_purchase(self, name: str, purchase: Purchase):
        self.add_customer(name, [purchase])

    def add_purchases(self, name: str, purchases: List[Purchase]):
        self.add_customer(name, purchases)

    def calculate_price(self, purchases: List[Purchase]) -> float:
        calculated_price = 0
        for purchase in purchases:
                if purchase['price'] > self.tax_threshold:
                    taxed_price = purchase['price'] * (1 + self.tax_rate)
                    calculated_price += taxed_price
                else:
                    calculated_price += purchase['price']

        return calculated_price

    def discount_eligibility(self, price: float):
        
        eligible = price > self.discount_eligibility
        
        if eligible:
            print("Eligible for discount")
        else:
            if price > 300:
                print("Potential future discount customer")
            else:
                print("No discount")
        
        if price > 1000:
            print("VIP Customer!")
        elif price > 800:
            print("Priority Customer")

    def generate_report(self):
        for name, purchases in self.customers.items():
            calculated_price = self.calculate_price(purchases)

            print(name)
            self.discount_eligibility(calculated_price)

    def calculate_shipping_fee(self, purchases: List[Purchase]):
        heavy_item = False
        for purchase in purchases:
            if purchase.get('weight', 0) > 20:
                heavy_item = True
                break
        if heavy_item:
            return 50
        else:
            return 20

    def calculate_shipping_fee_for_heavy_items(purchases: List[Purchase]):
        for purchase in purchases:
            if purchase.get('weight', 0) > 20:
                return 50
        return 20

    def calculate_shipping_fee_for_fragile_items(purchases: List[Purchase]):
        fragile_item = False
        for purchase in purchases:
            if purchase.get('fragile', False):
                fragile_item = True
                break
        if fragile_item:
            return 60
        else:
            return 25