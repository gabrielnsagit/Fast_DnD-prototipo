class RacaBase:
    def __init__(self, nome_raca, idade_max, idade_min, tamanho_max, tamanho_min, peso_max, peso_min, deslocamento):
        # Pré-Definições de Raça:
        self.__nomeRaca__ = nome_raca
        self.__tamanhos__ = [tamanho_min, tamanho_max]
        self.__idades__ = [idade_min, idade_max]
        self.__pesos__ = [peso_min, peso_max]
        self.__desloc__ = deslocamento
        ##############################################

        self.__nome__ = self.__setNome__()
        self.__idade__ = self.__setIdade__()
        self.__tamanho__ = self.__setTamanho__()
        self.__peso__ = self.__setPeso__()

    def __setTamanho__(self):
        while True:
            tamanho = float(input("\nEntre com o tamanho do {} em metros: ".format(self.__nomeRaca__)))
            if self.__tamanhos__[0] <= tamanho <= self.__tamanhos__[1]:
                return tamanho
            else:
                print("-" * 50)
                print('A altura recomendada esta entre {} e {} metros.'.format(self.__tamanhos__[0],
                                                                               self.__tamanhos__[1]))
                print("-" * 50)
                opcao = input('Deseja manter a altura escolhida? (s/n)\n')
                if opcao == 's':
                    return tamanho

    def __setIdade__(self):
        while True:
            idade = int(input("\nEntre com a idade do {}: ".format(self.__nomeRaca__)))
            if self.__idades__[0] <= idade <= self.__idades__[1]:
                return idade
            else:
                print("-" * 50)
                print('A idade recomendada esta entre {} e {}.'.format(self.__idades__[0], self.__idades__[1]))
                print("-" * 50)
                opcao = input('Deseja manter a idade escolhida? (s/n)\n')
                if opcao == 's':
                    return idade

    def __setPeso__(self):
        while True:
            peso = int(input("\nEntre com o peso do {} em kg: ".format(self.__nomeRaca__)))
            if self.__pesos__[0] <= peso <= self.__pesos__[1]:
                return peso
            else:
                print("-"*50)
                print('O peso recomendado esta entre {} e {}kg.'.format(self.__pesos__[0], self.__pesos__[1]))
                print("-" * 50)
                opcao = input('Deseja manter o peso escolhido? (s/n)\n')
                if opcao == 's':
                    return peso

    def __setNome__(self):
        return input('Entre com o nome do {}: '.format(self.__nomeRaca__))  # TRATAMENTO DE ERRO NECESSARIO

    # GETTERS

    def get_nome_pj(self):
        return self.__nome__

    def get_nome_raca(self):
        return self.__nomeRaca__
