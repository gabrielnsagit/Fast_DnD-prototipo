from .racaBase import RacaBase
from trataErro import pega_num


class MeioOrc(RacaBase):
    def __init__(self):
        super().__init__('Meio-Orc', 75, 14, 2.1, 1.8, 102, 70, 9)
        self.__modificadores__ = []
        self.__subraca__ = None
        self.__idSub__ = None
        self.__habilidades__ = self.__vantagens__()

    def __vantagens__(self):
        habilidades = ['Visao no Escuro', 'Ameacador', 'Resistencia Implacavel', 'Ataques Selvagens']
        atr1 = None
        self.__modificadores__ = [2, 0, 0, 0, 0, 0, 0, 0]
        print("Escolha dois dos atributos abaixo para aumentar em 1 ponto:")
        print("2 - DES")
        print("3 - CON")
        print("4 - INT")
        print("5 - SAB")
        print("6 - CAR")

        loop = True
        while loop:
            print("Escolha dois dos atributos abaixo para aumentar em 1 ponto:")
            print("2 - DES")
            print("3 - CON")
            print("4 - INT")
            print("5 - SAB")
            print("6 - CAR")
            print('Primeiro atributo: ')
            atr1 = pega_num()
            if atr1 in [2, 3, 4, 5, 6]:
                loop = False
            else:
                print('Opção invalida.\n')

        loop = True
        while loop:
            print('Segundo atributo: ')
            atr2 = pega_num()
            if atr1 == atr2:
                print('Este atributo já foi escolhido. Escolha outro da lista.')
                print("2 - DES")
                print("3 - CON")
                print("4 - INT")
                print("5 - SAB")
                print("6 - CAR")
            elif atr2 not in [2, 3, 4, 5, 6]:
                print('Opção invalida.\n')
            else:
                self.__modificadores__[atr1-1] += 1
                self.__modificadores__[atr2-1] += 1
                return habilidades

    # GETTERS #

    def get_modificadores(self):
        return self.__modificadores__
