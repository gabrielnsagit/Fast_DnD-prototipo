from .racaBase import RacaBase


class Tiefling(RacaBase):
    def __init__(self):
        super().__init__('Humano', 110, 17, 1.8, 1.5, 90, 60, 9)
        self.__modificadores__ = []
        self.__subraca__ = None
        self.__idSub__ = None
        self.__habilidades__ = self.__vantagens__()

    def __vantagens__(self):
        habilidades = ['Visao no Escuro', 'Resistencia Infernal', 'Legado Infernal']
        self.__modificadores__ = [0, 0, 0, 1, 0, 2, 0, 0]
        return habilidades

    # GETTERS #

    def get_modificadores(self):
        return self.__modificadores__
