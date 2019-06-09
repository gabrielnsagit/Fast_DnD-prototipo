from .racaBase import RacaBase
from trataErro import pega_num


class Halfling(RacaBase):
    def __init__(self):
        super().__init__('Halfling', 150, 20, 1.0, 0.8, 30, 15, 15/2)
        self.__modificadores__ = []
        self.__subraca__ = self.__setSubRaca__()
        self.__idSub__ = self.__setIdSub__()
        self.__habilidades__ = self.__vantagens__()

    @staticmethod
    def __setSubRaca__():

        while True:
            print('\nEscolha a Sub-Raça do Halfling:')
            print('1 - Pes-Leves')
            print('2 - Robusto')

            opcao = pega_num()

            if opcao in [1, 2]:
                return opcao

            print("-" * 50)
            print('Digite 1 ou 2.')
            print("-" * 50)

    def __setIdSub__(self):
        if self.__subraca__ == 1:
            return 6
        else:
            return 7

    def __vantagens__(self):
        habilidades = ["Sortudo", "Bravura", "Agilidade Halfling"]

        if self.__idSub__ == 6:
            self.__modificadores__ = [0, 2, 0, 0, 0, 1, 0, 0]
            habilidades.append("Furtividade Natural")

        else:
            self.__modificadores__ = [0, 2, 1, 0, 0, 0, 0, 0]
            habilidades.append("Resiliencia dos Robustos")

        return habilidades

    # GETTERS
    def get_modificadores(self):
        return self.__modificadores__
