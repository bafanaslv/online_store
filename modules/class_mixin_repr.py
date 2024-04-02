# Mixim срабатывающий при создании экземпляра класса.
# Миксин универсальный и выводит только строковые и числовые атрибуты. Списки не выводит.

class MixinRepr:
    def __init__(self, *args):
        print(repr(self))

    def __repr__(self):
        rep_str = f'{self.__class__.__name__}('
        for key in self.__dict__:
            if type(self.__dict__[key]) is str:
                rep_str += f'"{self.__dict__[key]}", '
            elif type(self.__dict__[key]) is int:
                rep_str += f'{self.__dict__[key]}, '
            elif type(self.__dict__[key]) is float:
                rep_str += f'{self.__dict__[key]}, '
        print(f'Создан объект:  {rep_str.rstrip()[:-1]})')
