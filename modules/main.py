# Программа предназначена для работы интернет магазина.

import os
from modules.class_category import Category
from config import ROOT_DIR
from ulils import load_json_file, create_category_objects


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
    dict_new_product = {"name": "Iphone 15", "description": "512GB", "price": 200000.0, "quantity": 6}
    Category.add_product(category_objects[0], dict_new_product)
    print(category_objects[0].product)
    print(category_objects[0])
    print(category_objects[0].product[0])
    print(category_objects[0].product[0] + category_objects[0].product[1])
    print(f'Количество категорий товаров - {Category.category_quantity}')
    print(f'Количество наименований уникальных товаров - {Category.product_names_quantity}')


if __name__ == '__main__':
    main(PRODUCTS_JSON_FILE, FILE)
