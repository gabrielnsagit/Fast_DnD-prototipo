from .classeBase import ClasseBase


class Barabaro(ClasseBase):
    def __init__(self):
        super().__init__()
        self.__nivel__ = 1
        self.__hp_base__ = 12
        self.__vida_base__ = [12, 0]


    def hp_up(self):
        return None

    def get_vida_base(self):
        return self.__vida_base__
