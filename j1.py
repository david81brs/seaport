#!/usr/bin/python3
# -*- coding: utf-8 -*-

soma=0
def jogador2():
    global soma
    n=int(input("Jogador 2: "))
    if n == 0:
        return
    soma = soma+n
    print(soma)
    return jogador1()


def jogador1():
    global soma
    n=int(input("Jogador 1: "))
    if n == 0:
        return
    soma=soma+n
    print(soma)
    return jogador2()


jogador1()
