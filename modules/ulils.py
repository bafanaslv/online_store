import json
import os
from modules.class_category import Category
from modules.class_product import Product

# product_objects - общий список объектов товаров
product_objects = []

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
    # category_objects - список объектов категорий
    # cat_prod_objects - список продуктов для текущей категории
    cat_prod_objects = []
    category_objects = []
    for ct_object in category_list:
        i = 0
        for product in ct_object.get("products"):
            object_product = Product(**product)
            product_objects.append(object_product)
            cat_prod_objects.append(product_objects[i])
            i += 1
        object_category = Category(ct_object.get("name"), ct_object.get("description"), cat_prod_objects)
        category_objects.append(object_category)
    return category_objects, product_objects
