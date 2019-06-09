def pega_num(texto):
    opcao = None
    loop = True
    while loop:
        try:
            opcao = int(input("{}: ".format(texto)))
        except ValueError:
            print("Digite um número.\n")
        else:
            loop = False
    return opcao
