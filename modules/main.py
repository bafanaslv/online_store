# Программа предназначена для работы интернет магазина.

import os
from modules.class_product import SmartPhone, Product, LawnGrass
from modules.class_category import Category
from modules.class_order import Order
from modules.class_iter_pruducts import IterProducts
from modules.class_iter_category import IterCategory
from config import ROOT_DIR
from ulils import load_json_file, create_category_objects
from modules.class_empty_quantity import EmptyQuantity

FILE = 'products.json'
PRODUCTS_JSON_FILE = os.path.join(ROOT_DIR, 'data', FILE)


def main(path, file_name):
    # Функция load_json_file загружает json- файл.
    # Функция create_category_objects формирует список категорий товаров category_objects.
    # dict_new_product - словарь с атрибутами нового товара.
    category_list = load_json_file(path, file_name)
    category_objects = []
    if category_list is not None:
        category_objects = create_category_objects(category_list)

    # Отработка геттера product класса Catofory.
    print(category_objects[0].product)

    # Отработка метода __str__ класса Catofory.
    print(category_objects[0])

    # Суммирование экземпляров товаров одного класса.
    print(category_objects[0].product_objects[0] + category_objects[0].product_objects[1])

    # Добавление нового товара в категорию.
    dict_new_product = {"name": "Iphone 15", "description": "512GB", "price": 200000.0, "quantity": 6, "color": "Белый"}
    new_product = Product.new_product(dict_new_product)
    Category.add_product(category_objects[0], new_product)

    # Суммирование экземпляров товаров разных классов.
    new_lawngrass = LawnGrass("Трава", "Газонная", 2100.0, 8,
                              "зеленый", "Россия", 2)
    #print(category_objects[0].product_objects[0] + new_lawngrass)

    # Вывод атрибутов класса Catogory.
    print(f'Количество категорий товаров: {Category.category_quantity}')
    print(f'Количество наименований уникальных товаров: {Category.product_names_quantity}\n')

    # Перебор продуктов в категории category_objects[0]
    for product in IterProducts(category_objects[0]):
        print(product)

    print('')
    #  Добавление товара с нулевым количеством в Заказы.
    dict_new_product = {"name": "Iphone 14", "description": "512GB", "price": 200000.0, "quantity": 0,
                        "color": "Белый", "capacity": 190, "model": "14", "memory": 32}
    try:
        new_product = SmartPhone.new_product(dict_new_product)
    except EmptyQuantity:
        print(f'{new_product.name}: нельзя добавить товар с нулевым количеством !')
    else:
        prod = Order(new_product)
        print(prod.__str__())
        print('Товар добавлен.')
    finally:
        print(f'Обработка добавления товара завершена.\n')

    # Перебор в списке категорий category_objects.
    for category_index in IterCategory(category_objects):
        print(category_objects[category_index].average_price())
    print('')

    # Добавление товара с нулевым количеством в категорию Продукты.
    dict_new_product = {"name": "Iphone 16", "description": "512GB", "price": 200000.0, "quantity": 0, "color": "Белый"}
    try:
        new_product = Product.new_product(dict_new_product)
    except EmptyQuantity:
        print(f'{new_product.name}: нельзя добавить товар с нулевым количеством !')
    else:
        Category.add_product(category_objects[0], new_product)
        print('Товар добавлен.')
    finally:
        print(f'Обработка добавления товара завершена.\n')

if __name__ == '__main__':
    main(PRODUCTS_JSON_FILE, FILE)
