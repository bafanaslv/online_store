from modules.class_product import Product


class Category:
    """Класс предназначен описания и поведения категорий товаров. name - наименование,
    description - описание, products - список товаров по данной категории,
    category_quantity - количество категорий."""
    name: str
    description: str
    products: list

    category_quantity = 0
    product_names_quantity = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_quantity += 1
        Category.product_names_quantity += len(self.__products)

    @property
    def product(self):
        """Геттер для вывода списка товаров для данной категории"""
        prod_list = ''
        for prod in self.__products:
            prod_list += str(prod)+'\n'
        return prod_list

    def add_product(self, dict_new_product):
        """Метод предназначен для добавление нового товара в категорию. Если наимнования товара совпадает с имеющимся
        товаром, то увеличивается количество и при необходимости корректируется цена товара."""
        # str_product - строка с атрибутами товара разделенные с символами ": ".
        # dict_new_product - словарь с атрибутами нового товара
        found_product = self.search_product(dict_new_product["name"], self.__products)
        if found_product is None:
            # если товар не нашелся в списке, то с помощью класса Product получаем новый экземпляр и добавляем его
            # в список товаров текущей категории.
            new_product = Product.new_product(dict_new_product)
            self.__products.append(new_product)
            Category.product_names_quantity += 1
        else:
            # если товар нашелся, то увеличиваем его количество и, при необходимости, корректируем цену.
            found_product.quantity += dict_new_product["quantity"]
            if dict_new_product["price"] != found_product.product_price:
                if dict_new_product["price"] < found_product.product_price:
                    if input(f'Вы согласны на понижение цены товара "{found_product.name}" ?\n') == 'y':
                        found_product.product_price = dict_new_product["price"]

    @staticmethod
    def search_product(prod_name, products):
        """Статический метод для поиска в списке объектов товаров по наименованию.
        Возвращает найденный объект или None если поиск неудачен."""
        for product in products:
            if prod_name == product.name:
                return product

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        """Метод посчитывает общий остаток продуктов определенной категории на складе."""
        quantity_products = 0
        for product in self.__products:
            quantity_products += product.quantity
        return quantity_products
