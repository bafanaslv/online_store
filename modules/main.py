# Программа предназначена для работы интернет магазина.

import os
from modules.class_category import Category
from config import ROOT_DIR
from ulils import load_json_file, create_category_objects


FILE = 'products.json'
PRODUCTS_JSON_FILE = os.path.join(ROOT_DIR, 'data', FILE)

def main(path, file_name):
    # Функция load_json_file загружает json- файл.
    # Функция create_category_objects формирует список категорий товаров.
    category_list = load_json_file(path, file_name)
    if category_list is not None:
        category_objects, product_objects = create_category_objects(category_list)
    Category.add_product(category_objects[0], product_objects, 'Iphone 15: 512GB, Gray space: 200000.0: 6')
    print(category_objects[0].product)
    print(f'Количество категорий продуктов - {Category.category_quantity}')
    print(f'Количество наименований уникальных продуктов - {Category.product_names_quantity}')

if __name__ == '__main__':
    main(PRODUCTS_JSON_FILE, FILE)
