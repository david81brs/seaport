#!/usr/bin/python3
# -*- coding: utf-8 -*-

#!/usr/bin/python3
# -*- coding: utf-8 -*-

def computador_escolhe_jogada(pecas,jogada_maxima):
    escolha = 0
    if jogada_maxima>=1 and jogada_maxima <=pecas:
        
        for jogada_teste in range(jogada_maxima,0,-1):
            resto = pecas % jogada_teste
            print('pecas %d jt: %d resto: %d jm: %d multiplo (%d+1): %d ' 
                % (pecas, jogada_teste, resto, jogada_maxima, jogada_maxima,resto/(jogada_maxima+1)))
            if (pecas - jogada_teste) % (jogada_maxima+1) == 0 :
                escolha = jogada_teste
            else:
                escolha = jogada_maxima
    else:
        escolha = pecas

    return escolha

resultado=computador_escolhe_jogada(5,3)
print("ANSWER %i" % resultado)