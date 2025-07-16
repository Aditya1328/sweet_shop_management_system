import pytest
from sweet_shop import Sweet, SweetShop

def test_add_sweet():
    shop = SweetShop()
    sweet = Sweet(id=1, name='Ladoo', category='candy', price=10.0, quantity=50)
    shop.add_sweet(sweet)
    assert shop.get_sweet(1).name == 'Ladoo'

def test_delete_sweet():
    shop = SweetShop()
    sweet = Sweet(id=2, name='Barfi', category='pastry', price=15.0, quantity=20)
    shop.add_sweet(sweet)
    shop.delete_sweet(2)
    assert shop.get_sweet(2) is None