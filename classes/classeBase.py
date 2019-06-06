class ClasseBase:
    def __init__(self):
        self.__nivel__ = 1
        self.__xp__ = 0
        self.__proficiencia__ = 2


    def ganho_xp(self):
        nivel = self.__nivel__
        print('Menu: ')
        print('1 - Adicionar Experiencia')
        print('2 - Definir Experiencia')
        opcao = int(input('Opcao: '))

        if opcao == 1:
            self.__xp__ += int(input('Adicionar Experiencia: '))
        elif opcao == 2:
            self.__xp__ = int(input('Definir Experiencia: '))

        if 0 <= self.__xp__ < 300:
            self.__nivel__ = 1
            self.__proficiencia__ = 2
        elif 300 <= self.__xp__ < 900:
            self.__nivel__ = 2
            self.__proficiencia__ = 2

        elif 900 <= self.__xp__ < 2700:
            self.__nivel__ = 3
            self.__proficiencia__ = 2

        elif 2700 <= self.__xp__ < 6500:
            self.__nivel__ = 4
            self.__proficiencia__ = 2

        elif 6500 <= self.__xp__ < 14000:
            self.__nivel__ = 5
            self.__proficiencia__ = 3

        elif 14000 <= self.__xp__ < 23000:
            self.__nivel__ = 6
            self.__proficiencia__ = 3

        elif 23000 <= self.__xp__ < 34000:
            self.__nivel__ = 7
            self.__proficiencia__ = 3

        elif 34000 <= self.__xp__ < 48000:
            self.__nivel__ = 8
            self.__proficiencia__ = 3

        elif 48000 <= self.__xp__ < 64000:
            self.__nivel__ = 9
            self.__proficiencia__ = 4

        elif 64000 <= self.__xp__ < 85000:
            self.__nivel__ = 10
            self.__proficiencia__ = 4

        elif 85000 <= self.__xp__ < 100000:
            self.__nivel__ = 11
            self.__proficiencia__ = 4

        elif 100000 <= self.__xp__ < 120000:
            self.__nivel__ = 12
            self.__proficiencia__ = 4

        elif 120000 <= self.__xp__ < 140000:
            self.__nivel__ = 13
            self.__proficiencia__ = 5

        elif 140000 <= self.__xp__ < 165000:
            self.__nivel__ = 14
            self.__proficiencia__ = 5

        elif 165000 <= self.__xp__ < 195000:
            self.__nivel__ = 15
            self.__proficiencia__ = 5

        elif 195000 <= self.__xp__ < 225000:
            self.__nivel__ = 16
            self.__proficiencia__ = 5

        elif 225000 <= self.__xp__ < 265000:
            self.__nivel__ = 17
            self.__proficiencia__ = 6

        elif 265000 <= self.__xp__ < 305000:
            self.__nivel__ = 18
            self.__proficiencia__ = 6

        elif 305000 <= self.__xp__ < 355000:
            self.__nivel__ = 19
            self.__proficiencia__ = 6

        else:
            self.__nivel__ = 20
            self.__proficiencia__ = 6

        if nivel < self.__nivel__:
            self.__level_up__()

    def __level_up__(self):
        print('LEVEL UP!')

    def get_proficiencia(self):
        return self.__proficiencia__
