from abstract_classes import Categoryabc


class Order(Categoryabc):
    """ Класс предназначен для описания покупки товара определенной категории и расчета остатка товара после покупки."""
    product: object

    def __init__(self, product):
        self.product = product
        self.amount = product.price * product.quantity

    def add_product(self, product):
        print(self.__name__)
        print(f'Куплен товар: {product.name}, {product.quantity} '
              f'шт. на сумму - {product.product_price * product.quantity}')

    def __len__(self):
        pass
