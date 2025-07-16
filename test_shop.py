import pytest
from sweet_shop import Sweet, SweetShop

def test_add_sweet():
    shop = SweetShop()
    # Adding sweet
    sweet = Sweet(id=1, name='Ladoo', category='candy', price=10.0, quantity=50)
    shop.add_sweet(sweet)
    # Asserting the Adding Function
    assert shop.get_sweet(1).name == 'Ladoo'

def test_delete_sweet():
    shop = SweetShop()

    # Adding sweet with id=2
    sweet = Sweet(id=2, name='Barfi', category='pastry', price=15.0, quantity=20)
    shop.add_sweet(sweet)

    # Deleting Sweet with id=2
    shop.delete_sweet(2)

    #Asserting the Deleting Function
    assert shop.get_sweet(2) is None

def test_view_sweets():
    shop = SweetShop()
    shop.add_sweet(Sweet(id=3, name='Rasgulla', category='candy', price=12.0, quantity=30))
    shop.add_sweet(Sweet(id=4, name='Jalebi', category='candy', price=8.0, quantity=40))
    sweets = shop.view_sweets()
    assert len(sweets) == 2
    
    # Asserting view Function
    assert sweets[0].name == 'Rasgulla'
    assert sweets[1].name == 'Jalebi'

def test_search_sweets():
    shop = SweetShop()

    # Adding Sweets
    shop.add_sweet(Sweet(6, 'Chocolate Cake', 'chocolate', 50.0, 10))
    shop.add_sweet(Sweet(7, 'Candy Stick', 'candy', 5.0, 100))
    shop.add_sweet(Sweet(8, 'Pastry Delight', 'pastry', 30.0, 25))

    # Calling search Function
    by_name = shop.search(name='Candy Stick')
    by_category = shop.search(category='pastry')
    by_price = shop.search(price_range=(10, 55))

    # Asserting search function
    assert len(by_name) == 1 and by_name[0].name == 'Candy Stick'
    assert len(by_category) == 1 and by_category[0].name == 'Pastry Delight'
    assert len(by_price) == 2