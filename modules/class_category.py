from modules.class_product import Product
from modules.class_mixin_repr import MixinRepr
from modules.abstract_classes import Categoryabc
from modules.class_empty_quantity import EmptyQuantity

class Category(Categoryabc, MixinRepr):
    """Класс предназначен описания и поведения категорий товаров. name - наименование,
    description - описание, products - список товаров по данной категории,
    category_quantity - количество категорий, avg_price - средняя цена товаров данной категории."""
    name: str
    description: str
    products: list
    category_quantity = 0
    product_names_quantity = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        super().__repr__()
        Category.category_quantity += 1
        Category.product_names_quantity += len(self.__products)

    @property
    def product_objects(self):
        """Геттер для вывода списка товаров для данной категории"""
        return self.__products

    @property
    def product(self):
        """Геттер для вывода списка товаров для данной категории"""
        prod_list = ''
        for prod in self.__products:
            prod_list += str(prod)+'\n'
        return prod_list

    def add_product(self, new_product):
        """Метод предназначен для добавление нового товара в категорию. Если наименования товара совпадает с имеющимся
        товаром, то увеличивается количество и при необходимости корректируется цена товара."""

        # new_product - экземпляр нового товара.
        found_product = self.search_product(new_product.name, self.__products)
        if found_product is None:
            # если товар не нашелся в списке, то добавляем его в список товаров текущей категории.
            if not isinstance(new_product, Product):
                raise TypeError("Добавлять можно только объекты одного класса или его наследников.")
            if new_product.quantity == 0:
                raise EmptyQuantity
            self.__products.append(new_product)
            Category.product_names_quantity += 1
        else:
            # если товар нашелся, то увеличиваем его количество и, при необходимости, корректируем цену.
            found_product.quantity += new_product.quantity
            if new_product.product_price != found_product.product_price:
                if new_product.product_price < found_product.product_price:
                    if input(f'Вы согласны на понижение цены товара "{found_product.name}" ?\n') == 'y':
                        found_product.product_price = new_product.product_price

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

    def average_price(self):
        """ Метод предназначен для расчета средней цены товара по определенной категории."""
        sum_price = sum(prod.product_price for prod in self.__products)
        try:
            result = sum_price / len(self.__products)
        except ZeroDivisionError:
            return 0
        else:
            return f'Средняя цена товаров по категории {self.name}:  {round(result, 2)} р.'