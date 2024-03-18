# Программа предназначена для работы интернет магазина.

import os
from modules.class_category import Category
from config import ROOT_DIR
from ulils import load_json_file, create_category_objects

FILE = 'products.json'
PRODUCTS_JSON_FILE = os.path.join(ROOT_DIR, 'data', FILE)


def main(path, file_name):
    category_list = load_json_file(path, file_name)
    if category_list is not None:
        category_objects = create_category_objects(category_list)
        print(f'Количество категорий продуктов - {Category.category_quantity}')
        print(f'Количество наименований уникальных продуктов - {Category.product_names_quantity}')


if __name__ == '__main__':
    main(PRODUCTS_JSON_FILE, FILE)
