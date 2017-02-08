#!/usr/bin/python3
# -*- coding: utf-8 -*-

n=1

while n<=8:
    
    if n % 2 == 0:
        vez="C"
    else:
        vez="U"

    if n<=8 and vez=="C":
        print("Vez do computador")
    elif n<=8:
        print("Vez do usuário")
    n+=1

