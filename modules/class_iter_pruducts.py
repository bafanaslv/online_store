# Итератор для перебора в списке продуктов в экземпляре класса Category.

class IterProducts:
    def __init__(self, object_category):
        """Создается ссылка на спиское товаров в объекте Category."""
        self.products = object_category.product_objects

    def __iter__(self):
        """Метод устанавливает начальное занчение индекса в списке товаров и возвращает итератор."""
        self.current_product_index = -1
        return self

    def __next__(self):
        """Метод перебирает товары по индексу пока значение не достигнет количеству товаров минус единица."""
        if self.current_product_index + 1 < len(self.products):
            self.current_product_index += 1
            return self.products[self.current_product_index]
        else:
            raise StopIteration
