from .racaBase import RacaBase


class MeioElfo(RacaBase):
    def __init__(self):
        super().__init__('Meio-Elfo', 180, 20, 1.8, 1.5, 90, 60, 9)
        self.__modificadores__ = []
        self.__subraca__ = None
        self.__idSub__ = None
        self.__habilidades__ = self.__vantagens__()

    def __vantagens__(self):
        habilidades = ['Visao no Escuro', 'Ancestral Feerico', 'Versatilidade em Pericia']
        self.__modificadores__ = [0, 0, 0, 0, 0, 2, 0, 0]
        print("Escolha dois dos atributos abaixo para aumentar em 1 ponto:")
        print("1 - FOR")
        print("2 - DES")
        print("3 - CON")
        print("4 - INT")
        print("5 - SAB")
        atr1 = int(input('Primeiro atributo: '))
        atr2 = int(input('Segundo atributo: '))
        self.__modificadores__[atr1] += 1
        self.__modificadores__[atr2] += 1
        return habilidades

    # GETTERS

    def get_modificadores(self):
        return self.__modificadores__
