# Итератор для перебора в списке экземпляров класса Category.

class IterCategory:
    def __init__(self, object_category):
        """Создается ссылка на список объектов Category."""
        self.object_category = object_category

    def __iter__(self):
        """Метод устанавливает начальное занчение индекса в списке категорий и возвращает итератор."""
        self.current_index = -1
        return self

    def __next__(self):
        """Метод перебирает категории по индексу пока значение не достигнет количеству категорий минус единица."""
        if self.current_index + 1 < len(self.object_category):
            self.current_index += 1
            return self.current_index
        else:
            raise StopIteration
