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

    def __repr__(self):
        return f'{self.name}, цена: {self.price}, количество: {self.quantity}'