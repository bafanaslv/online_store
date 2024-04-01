# Mixim срабатывающий при создании экземпляра класса.

class MixinRepr:
    def __init__(self, *args):
        print(repr(self))

    def __repr__(self):
        rep_str = f'{self.__class__.__name__}('
        for key in self.__dict__:
            if type(self.__dict__[key]) is str:
                rep_str += f'"{self.__dict__[key]}", '
            else:
                rep_str += f'{self.__dict__[key]}, '
        print(f'"Создан объект: " {rep_str.rstrip()[:-1]})')
