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
    """Функция предназначена получения списка категорий товаров. Параллельно формируется список
    объектов товаров cat_prod_objects для аттрибута priducts."""
    # category_objects - список объектов категорий
    # cat_prod_list - список продуктов для текущей категории
    category_objects = []
    for category_object in category_list:
        cat_prod_list = []
        for product in category_object.get("products"):
            object_product = Product(**product)
            cat_prod_list.append(object_product)
        object_category = Category(category_object.get("name"), category_object.get("description"), cat_prod_list)
        category_objects.append(object_category)
    return category_objects
