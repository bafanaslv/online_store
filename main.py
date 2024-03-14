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


def create_products_objects(products_list):
    products_objects = []
    for pr_object in products_list:
        o = Category(pr_object.get("name"), pr_object.get("description"), pr_object.get("products"))
        products_objects.append(o)
    return products_objects


def main(path):
    products_list = load_json_file(path)
    if products_list is not None:
        products_objects = create_products_objects(products_list)
        print(products_objects)
        return True
    else:
        return None


if __name__ == '__main__':
    main(PRODUCTS_JSON_FILE)
