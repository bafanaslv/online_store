from abc import ABC, abstractmethod
from modules.class_mixin_repr import MixinRepr


class Productabc(ABC):
    @abstractmethod
    def new_product(self):
        pass

    @staticmethod
    def product_price(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Product(Productabc, MixinRepr):
    """Класс предназначен описания и поведения номенклатуры товаров. name - наименование,
    description - описание, price - цена, quantity - количество товара, color - цвет."""
    name: str
    description: str
    price: float
    quantity: int
    color: str

    def __init__(self, name, description, price, quantity, color):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color
        super().__repr__()

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

    def prod_info(self):
        return f'{self.__class__.__name__}({self.name}, {self.description}, {self.product_price}, {self.quantity})'

    def __add__(self, other):
        if isinstance(other, type(self)):
            return self.quantity * self.__price + other.quantity * other.__price
        raise TypeError('Складывать можно только продукты одиной категории !')


class SmartPhone(Product):
    """Класс предназначен для описания и поведения номенклатуры смартфонов и является дочерним от класса Product
    В описание добавились свойства: capacity - производительность, model - модель, memory - объем оперативной памяти,
     color - цвет."""
    capacity: float
    model: str
    memory: int

    def __init__(self, name, description, price, quantity, color, capacity, model, memory):
        self.capacity = capacity
        self.model = model
        self.memory = memory
        super().__init__(name, description, price, quantity, color)

    def prod_info(self):
        return f'{self.__class__.__name__}({self.name}, {self.description}, {self.product_price}, {self.quantity})'


class LawnGrass(Product):
    """Класс предназначен для описания и поведения номенклатуры газонной травы и является дочерним от класса Product
    В описание добавились свойства: country - страна-производитель, germination - срок прорастания, color - цвет."""
    country: str
    germination: int

    def __init__(self, name, description, price, quantity, color, country, germination):
        self.country = country
        self.germination = germination
        super().__init__(name, description, price, quantity, color)
