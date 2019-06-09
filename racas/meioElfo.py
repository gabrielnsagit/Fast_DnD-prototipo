from .racaBase import RacaBase
from trataErro import pega_num


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
        atr1 = None

        loop = True
        while loop:
            print("Escolha dois dos atributos abaixo para aumentar em 1 ponto:")
            print("1 - FOR")
            print("2 - DES")
            print("3 - CON")
            print("4 - INT")
            print("5 - SAB")
            print('Primeiro atributo: ')
            atr1 = pega_num('Opção')
            if atr1 in [1, 2, 3, 4, 5]:
                loop = False
            else:
                print('Opção invalida.\n')

        loop = True
        while loop:
            print('Segundo atributo: ')
            atr2 = pega_num('Opção')
            if atr1 == atr2:
                print('Este atributo já foi escolhido. Escolha outro da lista.')
                print("1 - FOR")
                print("2 - DES")
                print("3 - CON")
                print("4 - INT")
                print("5 - SAB")
            elif atr2 not in [1, 2, 3, 4, 5]:
                print('Opção invalida.\n')
            else:
                self.__modificadores__[atr1-1] += 1
                self.__modificadores__[atr2-1] += 1
                return habilidades

    # GETTERS

    def get_modificadores(self):
        return self.__modificadores__
