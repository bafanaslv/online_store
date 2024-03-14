# Программа предназначена для работы интернет магазина.

import json
import os
from classes import *


FILE = 'products.json'
PRODUCTS_JSON_FILE = os.path.join('data', FILE)


def load_json_file(path):
    """Загрузка json - файла интернет магазина."""
    if not os.path.exists(path):
        print(f'Файл {FILE} отсуствует или указан неверный путь к нему !\n')
        return None
    else:
        with open(path, 'r', encoding='utf-8') as file:
            try:
                print(f'Файл {FILE} успешно загружен  !')
                return json.load(file)
            except json.decoder.JSONDecodeError:
                print(f'Неверная структура файла {FILE} !')
                return None


def create_category_objects(category_list):
    """Функция предназначена получения списка категорий продуктов. Параллельно формируется
    список наименований продуктов product_objects."""
    category_objects = []
    for ct_object in category_list:
        ob_c = Category(ct_object.get("name"), ct_object.get("description"), ct_object.get("products"))
        category_objects.append(ob_c)
    return category_objects


def main(path):
    category_list = load_json_file(path)
    if category_list is not None:
        category_objects = create_category_objects(category_list)
        print(f'Количество категорий продуктов - {Category.category_quantity}')
        print(f'Количество наименований продуктов - {Product.product_quantity}')
        return True
    else:
        return None


if __name__ == '__main__':
    main(PRODUCTS_JSON_FILE)
