def pega_num():
    opcao = None
    loop = True
    while loop:
        try:
            opcao = int(input("Opção: "))
        except ValueError:
            print("Digite um número.\n")
        else:
            loop = False
    return opcao
