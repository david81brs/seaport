def n_primos(n):
    np=0
    fator=2
    while n % fator !=0 and fator<=n/2:
        fator+=1
        if n % fator == 0:
            pass
        else:
            np+=1
    return np
