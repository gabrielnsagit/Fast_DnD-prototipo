from .classeBase import ClasseBase
from trataErro import pega_num


class Bardo(ClasseBase):
    def __init__(self):
        super().__init__()
        self.__hp_base__ = 8  # + MODIFICADOR DE CONST -> SERÁ SOMADO POSTERIORMENTE
        self.__pericias__ = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__resist_test__ = [0, 1, 0, 0, 0, 1]
        self.__prof_armaduras__ = ['Armaduras leves']
        self.__prof_armas__ = ['Armas simples', 'Bestas de mao', 'Espadas longas', 'Rapieras', 'Espadas Curtas']
        # IMPLEMENTAR EQUIPAMENTOS POSTERIORMENTE
        self.__itens__ = ['Armadura de Couro', 'Adaga']
        self.__set_pericias__()

    def __set_pericias__(self):
        opcao1 = None

        print('Escolha três das perícias abaixo:')
        print(" 0 - Atletismo")
        print(" 1 - Acrobacia")
        print(" 2 - Furtividade")
        print(" 3 - Prestidigitação")
        print(" 4 - Arcanismo")
        print(" 5 - História")
        print(" 6 - Investigação")
        print(" 7 - Natureza")
        print(" 8 - Religião")
        print(" 9 - Adestrar Animais")
        print("10 - Intuição")
        print("11 - Medicina")
        print("12 - Percepção")
        print("13 - Sobrevivência")
        print("14 - Atuação")
        print("15 - Enganação")
        print("16 - Intimidação")
        print("17 - Persuasão")
        loop = True
        while loop:
            opcao1 = pega_num('Primeira opção')

            if opcao1 in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]:
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
                print(" 1 - Acrobacia")
                print(" 2 - Furtividade")
                print(" 3 - Prestidigitação")
                print(" 4 - Arcanismo")
                print(" 5 - História")
                print(" 6 - Investigação")
                print(" 7 - Natureza")
                print(" 8 - Religião")
                print(" 9 - Adestrar Animais")
                print("10 - Intuição")
                print("11 - Medicina")
                print("12 - Percepção")
                print("13 - Sobrevivência")
                print("14 - Atuação")
                print("15 - Enganação")
                print("16 - Intimidação")
                print("17 - Persuasão")
            elif opcao2 in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]:
                self.__pericias__[opcao2] = 1
                loop = False
            else:
                print('Opção inválida.')

        loop = True
        while loop:
            opcao3 = pega_num('Terceira opção')

            if opcao3 == opcao1 or opcao3 == opcao1:
                print('Perícia já escolhida. Escolha outra da lista:')
                print(" 0 - Atletismo")
                print(" 1 - Acrobacia")
                print(" 2 - Furtividade")
                print(" 3 - Prestidigitação")
                print(" 4 - Arcanismo")
                print(" 5 - História")
                print(" 6 - Investigação")
                print(" 7 - Natureza")
                print(" 8 - Religião")
                print(" 9 - Adestrar Animais")
                print("10 - Intuição")
                print("11 - Medicina")
                print("12 - Percepção")
                print("13 - Sobrevivência")
                print("14 - Atuação")
                print("15 - Enganação")
                print("16 - Intimidação")
                print("17 - Persuasão")
            elif opcao3 in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]:
                self.__pericias__[opcao3] = 1
                loop = False
            else:
                print('Opção inválida.')
