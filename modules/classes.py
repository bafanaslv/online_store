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
        self.products = products
        Category.category_quantity += 1
        Category.product_names_quantity += len(self.products)

    def __repr__(self):
        return self.name


class Product:
    """Класс предназначен описания и поведения номенклатуры продуктов. name - наименование,
    description - описание, price - цена, quantity - количество, product_names_quantity - количество наименований."""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f'{self.name}, цена: {self.price}, количество: {self.quantity}'
