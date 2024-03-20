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
        prod_list = ''
        for prod in self.__products:
            prod_list += f'{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n'
        return prod_list

    def add_product(self, str_product):
        prod_attr_list = list(str_product.split(": "))
        found_product = self.search_product(prod_attr_list[0], self.__products)
        if found_product is None:
            ob_pr = Product.new_product(prod_attr_list)
            self.__products.append(ob_pr)
            Category.product_names_quantity += 1
        else:
            found_product.quantity += int(prod_attr_list[3])
            if float(prod_attr_list[2]) <= 0:
                print(f'Введена неверная цена: {prod_attr_list[2]}')
            else:
                if float(prod_attr_list[2]) >= found_product.price:
                    Product.get_product = float(prod_attr_list[2])
                    found_product.price = float(prod_attr_list[2])
                else:
                    if input('Вы согласны на понижение цены товара ?') == 'y':
                        Product.get_product = float(prod_attr_list[2])
                        found_product.price = float(prod_attr_list[2])

    @staticmethod
    def search_product(prod_name, products):
        for product in products:
            if prod_name == product.name:
                return product

    def __repr__(self):
        return self.name
