from random import random


def rola_atributos():
    atributos = []
    for atributo in range(0, 6):
        dados = []
        for dado in range(0, 4):
            val_dado = int(((random()*50) % 6)) + 1
            dados.append(val_dado)
        menor = min(dados)
        dados.remove(menor)
        val_atributo = sum(dados)
        atributos.append(val_atributo)
    return atributos


def rola(qtd, faces):
    valores = []
    for i in range(0, qtd):
        val_dado = int(((random() * 50) % faces)) + 1
        valores.append(val_dado)
    soma = sum(valores)
    return soma
