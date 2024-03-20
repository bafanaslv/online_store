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
    def new_product(cls, list_prod):
        """метод формирует новый объект товар из поступившего списка list_prod с атрибутами тоывара."""
        return cls(list_prod[0], list_prod[2], list_prod[2], list_prod[3])

    @property
    def get_product(self):
        return self.price

    @get_product.setter
    def get_product(self, price):
        self.price = price

    def __repr__(self):
        return f'{self.name} {self.price}'
