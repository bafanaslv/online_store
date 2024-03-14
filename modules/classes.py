product_objects = []


class Category:
    name: str
    description: str
    products: list

    category_quantity = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.products = self.create_product_list(self.products)
        Category.category_quantity += 1

    @staticmethod
    def create_product_list(prod):
        category_product_list = []
        for pr_object in prod:
            ob_p = Product(pr_object.get("name"), pr_object.get("description"),
                           pr_object.get("price"), pr_object.get("quantity"))
            product_objects.append(ob_p)
            category_product_list.append(ob_p)
        return category_product_list

    def get_products(self):
        """Возвращает плательщика."""
        return self.products


class Product:
    name: str
    description: str
    price: float
    quantity: int

    product_quantity = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.product_quantity += 1
