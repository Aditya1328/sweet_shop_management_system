class Sweet:
    def __init__(self, id, name, category, price, quantity):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

# Creating class performing various functions like  add, delete, search, sort , purchase sweets
class SweetShop:
    def __init__(self):
        self.inventory = {}

# Creating Add Function to add sweets
    def add_sweet(self, sweet: Sweet):

        # If sweet is present in inventory or it is in stock then raise value error
        if sweet.id in self.inventory:
            raise ValueError("Sweet ID already exists.")
        
        # If not present then add it in inventory
        self.inventory[sweet.id] = sweet

# Creating Get Function to get data of sweets
    def get_sweet(self, sweet_id: int):
        return self.inventory.get(sweet_id)

# Creating delete Function to delete sweet    
    def delete_sweet(self, sweet_id: int):
        if sweet_id in self.inventory:
            del self.inventory[sweet_id]

# Creating view Function to view sweets
    def view_sweets(self):
        return list(self.inventory.values())

# Creating Search Function to search sweets by name or category or price range   
    def search(self, name=None, category=None, price_range=None):
        results = list(self.inventory.values())

        # Searching by name
        if name:
            results = [s for s in results if s.name == name]

        # Searching by category
        if category:
            results = [s for s in results if s.category == category]
        
        # Searching by price_range
        if price_range:
            low, high = price_range
            results = [s for s in results if low <= s.price <= high]

        return results

# Creating Sorting function to sort by fields like price,id etc..    
    def sort_by(self, field):
        return sorted(self.inventory.values(), key=lambda s: getattr(s, field))

# Creating purchasing function for users    
    def purchase(self, sweet_id: int, quantity: int):
        sweet = self.get_sweet(sweet_id)

        # If sweet is not present then raise value error
        if not sweet:
            raise ValueError("Sweet not found.")
        
        # if sweet is present but quantity is not sufficient then raise value error
        if sweet.quantity < quantity:
            raise ValueError("Insufficient stock.")
        
        # Else update quantity
        sweet.quantity -= quantity

# Creating restock function to add stock of given id
    def restock(self, sweet_id: int, quantity: int):

        # Getting sweet with its id
        sweet = self.get_sweet(sweet_id)

        # If sweet not present than raise value error
        if not sweet:
            raise ValueError("Sweet not found.")
        
        # If sweet present than add quantity
        sweet.quantity += quantity