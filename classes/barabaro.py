from .classeBase import ClasseBase
from trataErro import pega_num


class Barabaro(ClasseBase):
    def __init__(self):
        super().__init__()
        self.__nivel__ = 1
        self.__hp_base__ = 12           # + MODIFICADOR DE CONST -> SERÁ SOMADO POSTERIORMENTE
        self.__pericias__ = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__resist_test__ = [1, 0, 1, 0, 0, 0, 0]

        self.__set_pericias__()

    def __set_pericias__(self):
        opcao1 = None

        print('Escolha duas das perícias abaixo:')
        print(" 0 - Atletismo")
        print(" 7 - Natureza")
        print(" 9 - Adestrar Animais")
        print("12 - Percepção")
        print("13 - Sobrevivência")
        print("16 - Intimidação")
        loop = True
        while loop:
            opcao1 = pega_num('Primeira opção')

            if opcao1 in [0, 7, 9, 12, 13, 16]:
                self.__pericias__[opcao1] = 1
                loop = False
            else:
                print('\nOpção inválida.')

        loop = True
        while loop:
            opcao2 = pega_num('Segunda opção')

            if opcao2 == opcao1:
                print('Perícia já escolhida. Escolha outra da lista:')
                print(" 0 - Atletismo")
                print(" 7 - Natureza")
                print(" 9 - Adestrar Animais")
                print("12 - Percepção")
                print("13 - Sobrevivência")
                print("16 - Intimidação")
            elif opcao2 in [0, 7, 9, 12, 13, 16]:
                self.__pericias__[opcao2] = 1
                loop = False
            else:
                print('Opção inválida.')
