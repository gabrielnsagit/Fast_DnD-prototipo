from .racaBase import RacaBase


class Draconato(RacaBase):
    def __init__(self):
        super().__init__('Draconato', 80, 15, 2.0, 1.7, 140, 110, 9)
        self.__modificadores__ = []
        self.__subraca__ = None
        self.__idSub__ = None
        self.__habilidades__ = self.__vantagens__()

    def __vantagens__(self):
        habilidades = []

        self.__modificadores__ = [1, 0, 0, 0, 0, 1, 0, 0]

        return habilidades

    def get_modificadores(self):
        return self.__modificadores__
