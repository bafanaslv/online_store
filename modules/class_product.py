class Product:
    """Класс предназначен описания и поведения номенклатуры продуктов. name - наименование,
    description - описание, price - цена, quantity - количество продукта."""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, str_product):
        name, description, price, quantity = str_product.split(', ')
        return cls(name, description, price, quantity)

    @property
    def get_product(self):
        return self.price

    @get_product.setter
    def get_product(self, price):
        self.price = price

    def __repr__(self):
        return f'{self.name} {self.price}'
