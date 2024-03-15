import pytest
from modules.classes import Category

category_list = [
    {
        "name": "Телевизоры",
        "description": "Современный телевизор, который позволяет наслаждаться просмотром",
        "products": [
            {
                "name": "55\" QLED 4K",
                "description": "Фоновая подсветка",
                "price": 123000,
                "quantity": 7
            }
        ]
    }
]


@pytest.fixture
def test_category_object():
    """Создается экземпляр класса Category и параллельно список экземпляров класса Product (products)."""
    return Category(category_list[0].get("name"),
                    category_list[0].get("description"),
                    category_list[0].get("products"))


def test_create_category_objects(test_category_object):
    """Проверка методов и аттрибутов классов Category & Product."""
    assert test_category_object.name == "Телевизоры"
    assert test_category_object.description == "Современный телевизор, который позволяет наслаждаться просмотром"
    assert type(test_category_object.products) is list
    assert Category.category_quantity == 1
    assert Category.product_names_quantity == 1
