#!/data/data/com.termux/files/usr/bin/python3
# -*- coding:utf-8 -*-

def maior_primo(n):
    primos=[]
    for i in range(1, n+1):
        c=0
        for k in range(1, n+1):
            #print(i, k, i % k)
            if i % k == 0:
                c+=1
        if c==2:
            #print("Primo %d"  % i)
            primos.append(i)
        else:
            #print("Nao primo %d"  % i)
            pass
    return primos[len(primos)-1]

