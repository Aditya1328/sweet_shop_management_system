import pytest
from sweet_shop import Sweet, SweetShop

def test_add_sweet():
    shop = SweetShop()
    sweet = Sweet(id=1, name='Ladoo', category='candy', price=10.0, quantity=50)
    shop.add_sweet(sweet)
    assert shop.get_sweet(1).name == 'Ladoo'