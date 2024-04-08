from abstract_classes import Categoryabc
from modules.class_empty_quantity import EmptyQuantity


class Order(Categoryabc):
    """ Класс предназначен для описания покупки товара определенной категории и расчета остатка товара после покупки."""
    def __init__(self, product):
        if product.quantity == 0:
            raise EmptyQuantity
        self.__product = product
        self.amount = product.product_price * product.quantity

    def __str__(self):
        return f'Куплен товар: {self.__product.name}, {self.__product.quantity} шт. на сумму - {self.amount}\n'

    def __len__(self):
        pass
