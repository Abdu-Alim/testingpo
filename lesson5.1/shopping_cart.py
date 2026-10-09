class ShoppingCart:
    def __init__(self):
        self.item = []

    def add_item(self, item, price):
        self.item.append({"item": item, "price": price})

    def get_total(self):
        return sum(item['price'] for item in self.item)
    