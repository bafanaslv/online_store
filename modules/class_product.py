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
    def price(self):
        return self.price

    @price.setter
    def price(self, price):
        if price >= 0:
            self.price = price
        else:
            print('Цена введена некорректно!')