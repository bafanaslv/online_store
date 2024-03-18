import json
import os
from modules.class_category import Category
from modules.class_product import Product


def load_json_file(path, file_name):
    """Загрузка json - файла интернет магазина."""
    if not os.path.exists(path):
        print(f'Файл {file_name} отсуствует или указан неверный путь к нему !\n')
    else:
        with open(path, 'r', encoding='utf-8') as file:
            try:
                print(f'Файл {file_name} успешно загружен !')
                return json.load(file)
            except json.decoder.JSONDecodeError:
                print(f'Неверная структура файла {file_name} !')


def create_category_objects(category_list):
    """Функция предназначена получения списка категорий продуктов."""
    category_objects = []
    for ct_object in category_list:
        ob_c = Category(ct_object.get("name"), ct_object.get("description"),
                        [Product(**product) for product in ct_object.get("products")])
        category_objects.append(ob_c)
    return category_objects
