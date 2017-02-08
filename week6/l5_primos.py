def eprimo(x):
    if x==2:
        return True
    fator=2
    while x % fator != 0 and fator<=x/2:
        fator+=1
    if x % fator == 0:
        return False
    else:
        return True

def n_primo(n):
    c=2
    np=0
    while c<=n:
        if eprimo(c):
            np+=1
        else:
            pass
        c+=1
    return np


