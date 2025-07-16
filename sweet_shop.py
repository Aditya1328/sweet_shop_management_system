class Sweet:
    def __init__(self, id, name, category, price, quantity):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

class SweetShop:
    def __init__(self):
        self.inventory = {}

    def add_sweet(self, sweet: Sweet):
        if sweet.id in self.inventory:
            raise ValueError("Sweet ID already exists.")
        self.inventory[sweet.id] = sweet

    def get_sweet(self, sweet_id: int):
        return self.inventory.get(sweet_id)