class Category:
    name: str
    description: str
    products: list

    category_quantity = 0
    product_quantity = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products


    def get_products(self):
        """Возвращает плательщика."""
        return self.products


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
