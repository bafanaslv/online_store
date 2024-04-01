# Mixim срабатывающий при создании экземпляра класса.

class MixinRepr:
    def __init__(self, *args):
        print(repr(self))

    def __repr__(self):
        rep = f'{self.__class__.__name__}('
        for key in self.__dict__:
            if type(self.__dict__[key]) is str:
                rep += f'"{self.__dict__[key]}", '
            else:
                rep += f'{self.__dict__[key]}, '
        print(rep.rstrip()[:-1] + ')')
