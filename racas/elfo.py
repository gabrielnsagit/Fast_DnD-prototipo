from .racaBase import RacaBase


class Elfo(RacaBase):
    def __init__(self):
        super().__init__('Elfo', 750, 100, 1.8, 1.5, 85, 65, 9)
        self.__modificadores__ = []
        self.__subraca__ = self.__setSubRaca__()
        self.__id__ = self.__setId__()
        self.__habilidades__ = self.__vantagens__()

    @staticmethod
    def __setSubRaca__():
        while True:
            print('\nEscolha a Sub-Raça do Elfo:')
            print('1 - Alto Elfo')
            print('2 - Elfo da Floresta')
            print('3 - Elfo Negro')
            opcao = int(input('Opcao: '))
            if opcao in [1, 2, 3]:
                return opcao
            print("-" * 50)
            print('Digite 1, 2 ou 3.')
            print("-" * 50)

    def __setId__(self):
        # Tratamento de Erros
        if self.__subraca__ == 1:
            return 3
        elif self.__subraca__ == 2:
            return 4
        else:
            return 5

    def __vantagens__(self):
        habilidades = ['Visao no Escuro', 'Sentidos Agucados', 'Ancestral Feerico', 'Trase']

        if self.__id__ == 3:
            self.__modificadores__ = [0, 2, 0, 1, 0, 0, 0, 0]
            habilidades.append('Treinamento Elfico com Armas')
            habilidades.append('Truque')
            habilidades.append('Idioma Adicional')
        if self.__id__ == 4:
            self.__modificadores__ = [0, 2, 0, 0, 1, 0, 0, 0]
            habilidades.append('Treinamento Elfico com Armas')
            habilidades.append('Pes Ligeiros')
            habilidades.append('Mascara da Natureza')
        else:
            self.__modificadores__ = [0, 2, 0, 0, 0, 1, 0, 0]
            habilidades.append('Visao no Escuro Superior')
            habilidades.append('Sensibilidade a Luz Solar')
            habilidades.append('Magia Drow')
            habilidades.append('Treinamento Drow com Armas')

        return habilidades

    # GETTERS

    def get_modificadores(self):
        return self.__modificadores__
