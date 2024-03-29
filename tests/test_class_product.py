import pytest
from modules.class_product import Product, LawnGrass

prod1 = {
    "name": "Samsung Galaxy C23 Ultra",
    "description": "256GB, Серый цвет, 200MP камера",
    "price": 180000.0,
    "quantity": 5,
    "color": "Серый"
}
prod2 = {
    "name": "Iphone 15",
    "description": "512GB, Gray space",
    "price": 210000.0,
    "quantity": 8,
    "color": "Gray"
}
prod3 = {
    "name": "Трава",
    "description": "Газонная",
    "price": 2100.0,
    "quantity": 8,
    "color": "зеленый",
    "country": "Россия",
    "germination": 2
}


@pytest.fixture
def test_product_object1():
    """Создается экземпляр класса Product."""
    return Product(prod1["name"],
                   prod1["description"],
                   prod1["price"],
                   prod1["quantity"],
                   prod1["color"])

@pytest.fixture
def test_product_object2():
    """Создается экземпляр класса Product."""
    return Product(prod2["name"],
                   prod2["description"],
                   prod2["price"],
                   prod2["quantity"],
                   prod3["color"])


@pytest.fixture
def test_product_object3():
    """Создается экземпляр класса Product."""
    return LawnGrass(prod3["name"],
                     prod3["description"],
                     prod3["price"],
                     prod3["quantity"],
                     prod3["color"],
                     prod3["country"],
                     prod3["germination"])



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


def test_products_add_(test_product_object1, test_product_object3):
    """Проверка сложение двух товаров."""
#    assert test_product_object1 + test_product_object2 == 2580000.0
    with pytest.raises(TypeError):
           Product.__add__(test_product_object1, test_product_object3)


def test_new_product(cl_product):
    """Проверка метода добавления нового товара в классе Product."""
    new_product = cl_product.new_product(prod2)
    assert new_product.name == "Iphone 15"
    assert new_product.description == "512GB, Gray space"
    assert new_product.product_price == 210000.0
    assert new_product.quantity == 8
