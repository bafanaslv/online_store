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

    def __repr__(self):
        return self.name
