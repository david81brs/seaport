#!/usr/bin/python3

def soma_hipotenusas(n):
    chipotenusa=1
    somahipot=[]
    while chipotenusa <=n:
        cat1 = 1
        while cat1 <=n:
            cat2=1
            cat1+=1
            while cat2 <=n:
                if (cat1**2 + cat2**2) == chipotenusa**2:
                    if chipotenusa not in somahipot:
                        somahipot.append(chipotenusa)
                   # print(cat1, cat2, chipotenusa, somahipot)
                cat2+=1
        chipotenusa+=1
    acumulador=0
    #print(somahipot)
    for i in range(0,len(somahipot)):
        acumulador=acumulador+somahipot[i]
    return acumulador
