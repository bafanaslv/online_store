import pytest
from modules.class_product import Product

prod1 = {
    "name": "Samsung Galaxy C23 Ultra",
    "description": "256GB, Серый цвет, 200MP камера",
    "price": 180000.0,
    "quantity": 5
}
prod2 = {
    "name": "Iphone 15",
    "description": "512GB, Gray space",
    "price": 210000.0,
    "quantity": 8
}


@pytest.fixture
def test_product_object1():
    """Создается экземпляр класса Product."""
    return Product(prod1["name"],
                   prod1["description"],
                   prod1["price"],
                   prod1["quantity"])


@pytest.fixture
def test_product_object2():
    """Создается экземпляр класса Product."""
    return Product(prod2["name"],
                   prod2["description"],
                   prod2["price"],
                   prod2["quantity"])


@pytest.fixture
def cl_product():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера",
                   180000.0, 5)


def test_create_category_objects(test_product_object1):
    """Проверка инициализацииy класса Product."""
    assert test_product_object1.name == "Samsung Galaxy C23 Ultra"
    assert test_product_object1.description == "256GB, Серый цвет, 200MP камера"
    assert test_product_object1.product_price == 180000.0
    assert test_product_object1.quantity == 5


def test_products_add_(test_product_object1, test_product_object2):
    """Проверка сложение двух товаров."""
    assert test_product_object1 + test_product_object2 == 2580000.0


def test_new_product(cl_product):
    """Проверка метода добавления нового товара в классе Product."""
    new_product = cl_product.new_product(prod2)
    assert new_product.name == "Iphone 15"
    assert new_product.description == "512GB, Gray space"
    assert new_product.product_price == 210000.0
    assert new_product.quantity == 8
