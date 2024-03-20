import pytest
from modules.class_product import Product

product_list = [
            {
                "name": "55\" QLED 4K",
                "description": "Фоновая подсветка",
                "price": 123000,
                "quantity": 7
            }
]


@pytest.fixture
def test_product_object():
    """Создается экземпляр класса Product."""
    return Product(product_list[0].get("name"),
                   product_list[0].get("description"),
                   product_list[0].get("price"),
                   product_list[0].get("quantity"))


def test_create_category_objects(test_product_object):
    """Проверка инициализацииy класса Product."""
    assert test_product_object.name == "55\" QLED 4K"
    assert test_product_object.description == "Фоновая подсветка"
    assert test_product_object.price == 123000
    assert test_product_object.quantity == 7
