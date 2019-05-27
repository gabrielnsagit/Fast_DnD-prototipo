class Pericias:
    def __init__(self, atributos, nome_raca):
        self.__pericias_dict__ = {1: 'Acrobacia', 2: 'Adestrar Animais', 3: 'Arcanismo', 4: 'Atletismo', 5: 'Atuacao',
                                  6: 'Enganacao', 7: 'Furtividade', 8: 'Historia', 9: 'Intimidacao', 10: 'Intuicao',
                                  11: 'Investigacao', 12: 'Medicina', 13: 'Natureza', 14: 'Percepcao', 15: 'Persuasao',
                                  16: 'Prestigitacao', 17: 'Religiao', 18: 'Sobrevivencia'}

        self.__dict_relacao__ = {1: 1, 2: 9, 3: 4, 4: 0, 5: 14, 6: 15, 7: 2, 8: 5, 9: 16, 10: 10, 11: 6, 12: 11, 13: 7,
                                 14: 12, 15: 17, 16: 3, 17: 8, 18: 13}

        self.__nome_raca__ = nome_raca
        self.__pericias__ = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__distribui_peric__()

        # Atletismo - 0
        self.__pericias__[0] += atributos[0]

        # Acrobacia - 1, Furtividade - 2, Prestidigitação - 3
        for i in range(1, 4):
            self.__pericias__[i] += atributos[1]

        # Arcanismo - 4, História - 5, Investigação - 6, Natureza - 7, Religião - 8
        for i in range(4, 9):
            self.__pericias__[i] += atributos[3]

        # Adestrar Animais - 9, Intuição - 10, Medicina - 11, Percepção - 12, Sobrevivência - 13
        for i in range(9, 14):
            self.__pericias__[i] += atributos[4]

        # Atuação - 14, Enganação - 15, Intimidação - 16, Persuasão - 17
        for i in range(14, 18):
            self.__pericias__[i] += atributos[5]

    def __menu_pericias__(self):
        for i in range(len(self.__pericias_dict__)):
            print("{0} - {1}".format(i + 1, self.__pericias_dict__[i + 1]))

    def __distribui_peric__(self):
        if self.__nome_raca__ == 'Humano':
            print('Escolha uma das pericias abaixo: ')
            self.__menu_pericias__()
            opcao = int(input('Opcao: '))
            print('Adquiriu pericia em {}'.format(self.__pericias_dict__[opcao]))
            self.__pericias__[self.__dict_relacao__[opcao]] = 1

        elif self.__nome_raca__ == 'Meio-Elfo':
            print('Escolha duas das pericias abaixo: ')
            self.__menu_pericias__()
            opcao1 = int(input('Primeira Opcao: '))
            opcao2 = int(input('Segunda Opcao: '))
            print('Adquiriu pericia em {0} e {1}'.format(self.__pericias_dict__[opcao1],
                                                         self.__pericias_dict__[opcao2]))
            self.__pericias__[self.__dict_relacao__[opcao1]] = 1
            self.__pericias__[self.__dict_relacao__[opcao2]] = 1

        for i in range(len(self.__pericias__)):
            self.__pericias__[i] *= 2               # ESSE 2 deve variar em funcao do nivel

    def print_pericias(self):
        print('-'*50)
        print('{:{align}{width}}'.format('PERICIAS', align='^', width='50'))
        print('-'*50)
        for i in range(len(self.__pericias__)):
            j = self.__dict_relacao__[i+1]
            print('{0:-<20}>|{1: >2}|'.format(self.__pericias_dict__[i+1], self.__pericias__[j]))

    def get_pericias(self):
        return self.__pericias__
