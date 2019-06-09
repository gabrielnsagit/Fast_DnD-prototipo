from .racaBase import RacaBase


class Humano(RacaBase):
    def __init__(self):
        super().__init__('Humano', 100, 17, 1.8, 1.5, 90, 60, 9)
        self.__modificadores__ = []
        self.__subraca__ = None
        self.__idSub__ = None
        self.__habilidades__ = self.__vantagens__()

    # MÉTODO ALTERA MODIFICADORES A SEREM SOMADOS COM OS ATRIBUTOS BASE, BEM COMO AS VANTAGENS (QUE HUMANOS NÃO RECEBEM)
    def __vantagens__(self):
        habilidades = []
        self.__modificadores__ = [1, 1, 1, 1, 1, 1, 0, 0]
        return habilidades

    # GETTERS #

    def get_modificadores(self):
        return self.__modificadores__
