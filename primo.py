#!/usr/bin/python3

def primo(n):
    c=0
    for i in range(n,1,-1):
        if n % i == 0:
            c+=1

