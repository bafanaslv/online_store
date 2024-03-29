import pytest
from modules.class_category import Category
from modules.class_product import Product
from modules.class_iter_pruducts import IterProducts


category_list = [
    {
        "name": "Смартфоны",
        "description": "Смартфоны, как средство не только коммуникации, но и получение "
                       "дополнительных функций для удобства жизни",
        "products": [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000,
                "quantity": 5,
                "color": "Серый"
            },
            {
                "name": "Iphone 15",
                "description": "512GB, Gray space",
                "price": 210000,
                "quantity": 8,
                "color": "Gray space"
            },
            {
                "name": "Xiaomi Redmi Note 11",
                "description": "1024GB, Синий",
                "price": 31000,
                "quantity": 14,
                "color": "Синий"
            }
        ]
    }
]


@pytest.fixture
def test_category_object():
    """Создается экземпляр класса Category."""
    return Category(category_list[0].get("name"),
                    category_list[0].get("description"),
                    [Product(**product) for product in category_list[0].get("products")])


@pytest.fixture
def cl_iterator(test_category_object):
    """Создаем эксземпляр итератора."""
    return IterProducts(test_category_object)


def test_class_iter_productions(cl_iterator):
    """Метод cl_iterator.__iter__() устанавливает указатель на первом элементе списка товаров
    и перебироем список методом __next__()."""
    cl_iterator.__iter__()
    assert cl_iterator.__next__().name == "Samsung Galaxy C23 Ultra"
    assert cl_iterator.__next__().name == "Iphone 15"
    assert cl_iterator.__next__().name == "Xiaomi Redmi Note 11"
