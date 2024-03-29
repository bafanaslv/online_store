import pytest
from modules.class_category import Category
from modules.class_product import Product

# new_lawngrass - словарь продукта Газонная трава.
new_lawngrass = {
    "name": "Трава",
    "description": "Газонная",
    "price": 2100.0,
    "quantity": 8,
    "color": "зеленый",
    "country": "Россия",
    "germination": 2
}


@pytest.fixture
def test_category_object():
    """Создается экземпляр класса Category."""
    return Category("Телевизоры", "Современный телевизор",
                    [Product("55\" QLED 4K", "Фоновая подсветка",
                             123000, 7, "Черный")])


def test_create_category_objects(test_category_object):
    """Проверка некоторых аттрибутов класса Category."""
    assert test_category_object.name == "Телевизоры"
    assert test_category_object.description == "Современный телевизор"
    assert Category.category_quantity == 1
    assert Category.product_names_quantity == 1


def test_category_add_product(test_category_object):
    """Проверка добавления товара из класса Газонная трава в список объектов класса Продукты."""
    with pytest.raises(TypeError):
        test_category_object.add_product(new_lawngrass)
