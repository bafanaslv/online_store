class Category:
    """Класс предназначен описания и поведения категорий продуктов. name - наименование,
    description - описание, products - список продуктов по данной категории,
    category_quantity - количество категорий."""
    name: str
    description: str
    products: list

    category_quantity = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_quantity += 1


class Product:
    """Класс предназначен описания и поведения номенклатуры продуктов. name - наименование,
    description - описание, price - цена, quantity - количество, product_names_quantity - количество наименований."""
    name: str
    description: str
    price: float
    quantity: int

    product_names_quantity = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.product_names_quantity += 1
