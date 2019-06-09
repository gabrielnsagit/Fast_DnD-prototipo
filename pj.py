import dado
from trataErro import pega_num
from racas.anao import Anao
from racas.elfo import Elfo
from racas.halfling import Halfling
from racas.humano import Humano
from racas.draconato import Draconato
from racas.gnomo import Gnomo
from racas.meioElfo import MeioElfo
from racas.meioOrc import MeioOrc
from racas.tiefling import Tiefling
from habilidades.pericias import Pericias
from classes.barabaro import Barabaro


class Pj:
    # DEFINICAO DE DICIONARIOS PARA INSTANCIACAO DE ATRIBUTOS DE CLASSES AGREGADAS

    classes = {1: "Barabaro", 2: "Bardo", 3: "Bruxo", 4: "Clerigo", 5: "Druida", 6: "Feiticeiro", 7: "Guerreiro",
               8: "Ladino", 9: "Mago", 10: "Monge", 11: "Paladino", 12: "Patrulheiro"}

    antecedentes = {1: "Acolito", 2: "Artesao", 3: "Artista", 4: "Charlatao", 5: "Criminoso", 6: "Eremita",
                    7: "Forasteiro", 8: "Heroi", 9: "Marinheiro", 10: "Nobre", 11: "Orfao", 12: "Sabio", 13: "Soldado"}
    ###################################################################################################################

    def __init__(self):
        self.__nomeJ__ = self.set_nome_j()

        self.__raca__ = self.__setRaca__()                      # Chama método para setar Raça

        self.__classe__ = self.__set_classe__()

        self.__atBase__ = self.__distribuir_pts__() + [0, 0]    # Atributos puramente distribuidos

        self.__atMod__ = self.__mod_atr__()  # Atributos com modificadores de raca, classe, etc...
        self.__modificadores__ = [-5 + int(self.__atMod__[0] // 2), -5 + int(self.__atMod__[1] // 2),
                                  -5 + int(self.__atMod__[2] // 2), -5 + int(self.__atMod__[3] // 2),
                                  -5 + int(self.__atMod__[4] // 2), -5 + int(self.__atMod__[5] // 2)]
        self.__pericias__ = Pericias(self.__modificadores__, self.__raca__.get_nome_raca(),
                                     self.__classe__.get_proficiencia())
        self.__antecedente__ = self.__set_antecedente__()
        self.__nomePj__ = self.__raca__.get_nome_pj()
        # Atributos na seguinte ordem:
        # FOR, DES, CON, INT, SAB, CAR, PV, CA
        self.__testResist__ = None
        self.__bonusProf__ = None
        self.__iniciativa__ = None

    @staticmethod
    def set_nome_j():
        return input("Entre com o nome do jogador: ")

    @staticmethod
    def __setRaca__():

        while True:
            print("Escolha uma das raças abaixo: ")
            print("1 - Anão")
            print("2 - Elfo")
            print("3 - Halfling")
            print("4 - Humano")
            print("5 - Draconato")
            print("6 - Gnomo")
            print("7 - Meio-Elfo")
            print("8 - Meio-Orc")
            print("9 - Tiefling")
            print()

            opcao = pega_num('Opção')

            if opcao in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                if opcao == 1:
                    raca = Anao()
                elif opcao == 2:
                    raca = Elfo()
                elif opcao == 3:
                    raca = Halfling()
                elif opcao == 4:
                    raca = Humano()
                elif opcao == 5:
                    raca = Draconato()
                elif opcao == 6:
                    raca = Gnomo()
                elif opcao == 7:
                    raca = MeioElfo()
                elif opcao == 8:
                    raca = MeioOrc()
                else:
                    raca = Tiefling()

                return raca
            else:
                print("Digite uma opcao valida.\n")

    @staticmethod
    def __set_classe__():
        while True:
            print("Escolha uma das classes abaixo: ")
            print("1 - Barbaro")
            print("2 - Bardo")
            print("3 - Bruxo")
            print("4 - Clerigo")
            print("5 - Druida")
            print("6 - Feiticeiro")
            print("7 - Guerreiro")
            print("8 - Ladino")
            print("9 - Mago")
            print("10 - Monge")
            print("11 - Paladino")
            print("12 - Patrulheiro")
            print()
            opcao = pega_num('Opção')

            if opcao in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                if opcao == 1:
                    classe = Barabaro()
                elif opcao == 2:
                    classe = Elfo()
                elif opcao == 3:
                    classe = Halfling()
                elif opcao == 4:
                    classe = Humano()
                elif opcao == 5:
                    classe = Draconato()
                elif opcao == 6:
                    classe = Gnomo()
                elif opcao == 7:
                    classe = MeioElfo()
                elif opcao == 8:
                    classe = MeioOrc()
                else:
                    classe = Tiefling()

                return classe
            else:
                print("Digite uma opcao valida.\n")

    @staticmethod
    def __set_antecedente__():
        while True:
            print("Escolha uma das classes abaixo: ")
            print("1 - Acolito")
            print("2 - Artesao de Guilda")
            print("3 - Artista")
            print("4 - Charlatao")
            print("5 - Criminoso")
            print("6 - Eremita")
            print("7 - Forasteiro")
            print("8 - Heroi do Povo")
            print("9 - Marinheiro")
            print("10 - Nobre")
            print("11 - Orfao")
            print("12 - Sabio")
            print("13 - Soldado")
            print()
            opcao = pega_num('Opção')

            if opcao in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
                return opcao                 # IMPLEMENTAR UM METODO PARA RETORNO DO ANTECEDENTE COMO UM OBJETO!!!!!!!!
            else:
                print("Digite uma opcao valida.\n")

    def __distribuir_pts__(self):
        opcao = 0
        atributos_val = [15, 14, 13, 12, 10, 8]
        final_atr = []

        while opcao not in [1, 2]:
            print("Defina a forma como quer distribuir os pontos:")
            print("1 - Atributos Predefinidos")
            print("2 - Rolagem de Dados")
            opcao = int(input("\nOpcao: "))

        if opcao == 1:
            final_atr = self.__aloca_pts__(atributos_val)

        if opcao == 2:
            atributos_val = dado.rola_atributos()  # CRIAR CLASSE DADO
            final_atr = self.__aloca_pts__(atributos_val)

        return final_atr

    @staticmethod
    def __aloca_pts__(atributos_val):
        final_atr = [0, 0, 0, 0, 0, 0]
        atributos_label = {1: "FOR", 2: "DES", 3: "CON", 4: "INT", 5: "SAB", 6: "CAR"}
        print("Seus pontos sao: {}, {}, {}, {}, {}, {}".format(atributos_val[0], atributos_val[1], atributos_val[2],
                                                               atributos_val[3], atributos_val[4], atributos_val[5]))
        print("Serao distibuidos nos atributos: ")
        print("1 - FOR")
        print("2 - DES")
        print("3 - CON")
        print("4 - INT")
        print("5 - SAB")
        print("6 - CAR\n")
        for i in range(len(atributos_val)):
            print('Colocar {0} pontos em que atributo?'.format(atributos_val[i]))
            ind_atr = int(input('Indice do Atributo: ')) - 1
            final_atr[ind_atr] = atributos_val[i]
            print('{0} pontos colocados em {1}.\n'.format(atributos_val[i], atributos_label[ind_atr+1]))

        return final_atr

    def __mod_atr__(self):
        atr_final = self.__raca__.get_modificadores()
        atr_final[6] += self.__classe__.get_vida_base()[0]
        atr_final[7] += self.__classe__.get_vida_base()[1]
        atr_final[6] += atr_final[2]
        for atr in range(len(self.__atBase__)):
            atr_final[atr] += self.__atBase__[atr]
        return atr_final

    def print_atributos(self):
        print('Força - {}\nDestreza - {}\nConstituição - {}\nInteligência - {}\nSabedoria - {}\nCarisma - {}\n'
              'Pontos de Vida - {}'.format(self.__atMod__[0], self.__atMod__[1], self.__atMod__[2], self.__atMod__[3],
                                           self.__atMod__[4], self.__atMod__[5], self.__atMod__[6]))


a = Pj()
a.print_atributos()
