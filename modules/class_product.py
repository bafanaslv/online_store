class Product:
    """Класс предназначен описания и поведения номенклатуры товаров. name - наименование,
    description - описание, price - цена, quantity - количество товара."""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_product):
        """Метод формирует новый объект товар из поступившего словаря dict_product с атрибутами товара."""
        return cls(**dict_product)

    @property
    def product_price(self):
        return self.__price

    @product_price.setter
    def product_price(self, price):
        if price <= 0:
            print(f'Неправильная цена товара: {price}\n')
        else:
            self.__price = price

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if type(self) is type(other):
            return self.quantity * self.__price + other.quantity * other.__price
        raise ValueError('Продукты должны быть из одного класса !')


class SmartPhone(Product):
    """Класс предназначен для описания и поведения номенклатуры смартфонов и является дочерним от класса Product
    В описание добавились свойства: capacity - производительность, model - модель, memory - объем оперативной памяти,
     color - цвет."""
    capacity: int
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, capacity, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.capacity = capacity
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс предназначен для описания и поведения номенклатуры газонной травы и является дочерним от класса Product
    В описание добавились свойства: country - страна-производитель, germination - срок прорастания, color - цвет."""
    country: str
    germination: int
    color: str

    def __init__(self, name, description, price, quantity, country, germination, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination = germination
        self.color = color
