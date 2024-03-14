# Программа предназначена для работы интернет магазина.

import json
import os
from classes import *


FILE = 'products.json'
PRODUCTS_JSON_FILE = os.path.join('data', FILE)


def load_json_file(path):
    if not os.path.exists(path):
        return None
    else:
        with open(path, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError:
                return None


def create_category_objects(category_list):
    category_objects = []
    for ct_object in category_list:
        ob_c = Category(ct_object.get("name"), ct_object.get("description"), ct_object.get("products"))
        category_objects.append(ob_c)
    return category_objects


def main(path):
    category_list = load_json_file(path)
    if category_list is not None:
        category_objects = create_category_objects(category_list)
        print(category_objects[0].get_products())
        print(category_objects[1].get_products())
        print(Category.category_quantity)
        print(Product.product_quantity)
        return True
    else:
        return None


if __name__ == '__main__':
    main(PRODUCTS_JSON_FILE)
