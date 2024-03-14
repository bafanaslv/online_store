import pytest
from main import Category, Product

test_category_objects = []
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
def test_category_list():
    """Создается экземпляр класса Category и параллельно список экземпляров класса Product (products)."""
    o = Category(category_list[0].get("name"),
                 category_list[0].get("description"),
                 category_list[0].get("products"))
    test_category_objects.append(o)
    return test_category_objects[0]


def test_create_category_objects(test_category_list):
    """Проверка методов и аттрибутов классов Category & Product."""
    assert test_category_objects[0].get_name() == "Телевизоры"
    assert test_category_objects[0].get_description() == ("Современный телевизор, который позволяет наслаждаться "
                                                          "просмотром")
    assert len(test_category_objects[0].get_products()) == 1
    assert Category.category_quantity == 1
    assert Product.product_quantity == 1
    assert test_category_objects[0].get_products()[0].get_name() == "55\" QLED 4K"
    assert test_category_objects[0].get_products()[0].get_description() == "Фоновая подсветка"
    assert test_category_objects[0].get_products()[0].get_price() == 123000
    assert test_category_objects[0].get_products()[0].get_quantity() == 7
