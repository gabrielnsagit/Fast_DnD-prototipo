from .racaBase import RacaBase
from trataErro import pega_num


class Gnomo(RacaBase):
    def __init__(self):
        super().__init__('Gnomo', 500, 40, 1.2, 0.9, 25, 15, 15/2)
        self.__modificadores__ = []
        self.__subraca__ = self.__setSubRaca__()
        self.__idSub__ = self.__setIdSub__()
        self.__habilidades__ = self.__vantagens__()

    @staticmethod
    def __setSubRaca__():
        while True:
            print('\nEscolha a Sub-Raca do Gnomo:')
            print('1 - Gnomo da Floresta')
            print('2 - Gnomo das Rochas')

            opcao = pega_num('Opção')

            if opcao in [1, 2]:
                return opcao
            print("-" * 50)
            print('Digite 1 ou 2.')
            print("-" * 50)

    def __setIdSub__(self):
        if self.__subraca__ == 1:
            return 8
        else:
            return 9

    def __vantagens__(self):

        habilidades = ['Esperteza Gnomica', 'Visao no Escuro']

        if self.__idSub__ == 8:
            self.__modificadores__ = [0, 1, 0, 2, 0, 0, 0, 0]
            habilidades.append('Ilusionista Nato')
            habilidades.append('Falar com bestas pequenas')

        else:
            self.__modificadores__ = [0, 0, 1, 2, 0, 0, 0, 0]
            habilidades.append('Conhecimento Artifice')
            habilidades.append('Engenhoqueiro')

        return habilidades

    # GETTERS #

    def get_modificadores(self):
        return self.__modificadores__
