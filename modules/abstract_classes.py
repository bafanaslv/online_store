from abc import ABC, abstractmethod


class Productabc(ABC):
    """ Абстарактный класс для класса Products и его дочерних классов."""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def new_product(self, dict_productt):
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


class Categoryabc(ABC):
    """ Абстарактный класс для классов Category и Order."""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def add_product(self, product):
        pass
