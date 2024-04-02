from abstract_classes import Categoryabc


class Order(Categoryabc):
    """ Класс предназначен для описания покупки товара определенной категории расчета остатка товара после покупки."""
    product: object
    amount: float

    def __init__(self, product):
        self.product = product
        self.amount = product.price * product.quantity

    def add_product(self, new_product):
        pass

    def __len__(self):
        pass
