from modules.class_product import Product

class Category:
    """Класс предназначен описания и поведения категорий продуктов. name - наименование,
    description - описание, products - список продуктов по данной категории,
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
        """геттер для вывода списка продуктов для данной категории товара"""
        prod_list = ''
        for prod in self.__products:
            prod_list += f'{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n'
        return prod_list

    def add_product(self, str_product):
        """Метод предназначен для добавление нового товара в категорию. Если наимнования товара совпадает с имеющимся
        товаром, то увеличивается количество и при необходимости корректируется цена товара."""
        # str_product - строка с атрибутами товара разделенные с символами ": ".
        # prod_attr_list - список с атрибутами товара, prod_attr_list[0] - наименование товара.
        prod_attr_list = list(str_product.split(": "))
        found_product = self.search_product(prod_attr_list[0], self.__products)
        if found_product is None:
            # если товар не нашелся в списке, то с помощью класса Product получаем новый экземпляр и добавляем его
            # в список товаров текущей категории.
            new_pr = Product.new_product(prod_attr_list)
            self.__products.append(new_pr)
            Category.product_names_quantity += 1
        else:
            # если товар нашелся, то увеличиваем его количество и, при необходимости, корректируем цену.
            found_product.quantity += int(prod_attr_list[3])
            if float(prod_attr_list[2]) <= 0:
                print(f'Введена неверная цена: {prod_attr_list[2]}')
            else:
                if float(prod_attr_list[2]) != found_product.price:
                    if float(prod_attr_list[2]) < found_product.price:
                        if input('Вы согласны на понижение цены товара ?\n') == 'n':
                            return
                    found_product.price = float(prod_attr_list[2])

    @staticmethod
    def search_product(prod_name, products):
        """Статический метод для поиска в списке объектов продуктов по наименование товара.
        Возвращает найденный объект или None если поиск неудачен."""
        for product in products:
            if prod_name == product.name:
                return product

    def __repr__(self):
        return self.name
