# product_objects - список обьектов класса Product.
product_objects = []


class Category:
    """Класс предназначен описания и поведения категорий продуктов. name - наименование,
    description - описание, products - список продуктов по данной категории
    (автоматически заполнятся при инициализации статическим методом create_product_list),
    category_quantity - количество категорий."""
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
        """Этот статический метод предназначен для получения общего списка product_objects экземпляпров класса
        Product и списка category_product_list для привязки к экземпляру категории."""
        category_product_list = []
        for pr_object in prod:
            ob_p = Product(pr_object.get("name"), pr_object.get("description"),
                           pr_object.get("price"), pr_object.get("quantity"))
            product_objects.append(ob_p)
            category_product_list.append(ob_p)
        return category_product_list

    def get_name(self):
        """Возвращает наименование категории продукта."""
        return self.name

    def get_description(self):
        """Возвращает наименование категории продукта."""
        return self.description

    def get_products(self):
        """Возвращает список продуктов."""
        return self.products


class Product:
    """Класс предназначен описания и поведения номенклатуры продуктов. name - наименование,
    description - описание, price - цена, quantity - количество, product_quantity - количество наименований."""
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

    def get_name(self):
        """Возвращает наименование продукта."""
        return self.name

    def get_description(self):
        """Возвращает описание продукта."""
        return self.description

    def get_price(self):
        """Возвращает цену продукта."""
        return self.price

    def get_quantity(self):
        """Возвращает количество продукта."""
        return self.quantity
