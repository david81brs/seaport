#!/usr/bin/python
largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

for i in range(0,altura):
    for k in range(0,largura):
        if i==0 or i==altura-1:
            print("#", end="")
    if i>0 and i<altura-1:
        print("#", end="")
        for l in range(0,largura-2):
            print(" ", end="")
        print("#", end="")
    print(end="\n")
