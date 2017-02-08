#!/usr/bin/python3

def maximo(x,y,z):
    valores=[]
    valores.append(x)
    valores.append(y)
    valores.append(z)
    valores.sort()
    return valores[len(valores)-1]


