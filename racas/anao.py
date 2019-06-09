from .racaBase import RacaBase
from trataErro import pega_num


class Anao(RacaBase):
    def __init__(self):
        super().__init__('Anao', 350, 50, 1.5, 1.2, 90, 75, 15/2)   # Inicia atributos de raça_base
        self.__modificadores__ = []
        self.__subraca__ = self.__setSubRaca__()
        self.__idSub__ = self.__setId__()
        self.__habilidades__ = self.__vantagens__()

    @staticmethod
    def __setSubRaca__():

        while True:
            print('\nEscolha a Sub-Raça do Anao:')
            print('1 - Anao da Colina')
            print('2 - Anao da Montanha')

            opcao = pega_num()

            if opcao in [1, 2]:
                return opcao

            print("-" * 50)
            print('Digite 1 ou 2.')
            print("-" * 50)

    def __setId__(self):
        return self.__subraca__

    def __vantagens__(self):
        habilidades = ['Visao no Escuro', 'Resiliencia Ana', 'Treinamento Anao em Combate',
                       'Proficiencia em Ferramenta', 'Especializacao em Rochas']

        # Valores de raça que serão somados aos atributos base.
        if self.__idSub__ == 1:
            self.__modificadores__ = [0, 0, 2, 0, 1, 0, 1, 0]
            habilidades.append("Tenacidade Ana")
        else:
            self.__modificadores__ = [2, 0, 2, 0, 0, 0, 0, 0]
            habilidades.append("Treinamento Anao com Armaduras")

        return habilidades

    # GETTERS

    def get_modificadores(self):
        return self.__modificadores__
