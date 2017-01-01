#!/usr/bin/python3
# -*- coding: utf-8 -*-

#rodada=1	# - Conta o número de rodadas.
#n = 0 		# - Registra o número de peças.
#m = 0		# - Registra o limite de peças por jogada.

def computador_escolhe_jogada(n, m):
    while True:
        if (n-m) % (m+1) == 0:
            return m
        else:
            m=m-1
            return m


def usuario_escolhe_jogada(n,m):
    while True:
        m_user=int(input("Quantas peças você vai tirar"))
	print(m_user)
	if m_user>m:
	    print("Oops! Jogada inválida! Tente de novo.")
	else:
            break
    return int(m_user)


def campeonato():
    rodada=1
    print("Quantas peças?")
    n = int(input())
    print("Limite de peças por jogada? ")
    m = int(input())
    while rodada<=3:
        if (n-m) % (m+1) == 0:
            print("Computador começa!")
        else:
            print("Você começa!")
        rodada+=1

def partida():

	print("Quantas peças?")
	n = int(input())
	print("Limite de peças por jogada? ")
	m = int(input())
	if (n-m) % (m+1) == 0:
		f=usuario_escolhe_jogada(n,m)
		n=n-f
	else:
		print("Computador começa!")
		f=computador_escolhe_jogada(n,m)
		n=n-f
	print("Fim de jogo!")



def main():
	print("Bem-vindo ao jogo do NIM! Escolha:")
	print("1 - para jogar uma partida isolada")
	print("2 - para jogar um campeonato", end=" ")
	choicy = input()

	if choicy=='2':
		print("Você escolheu um campeonato!")
                campeonato()
	elif choicy=='1':
		print("Você escolheu uma partida apenas.")
		partida()
	else:
		print("Você não escolheu nenhuma da opções.")




if __name__== '__main__':
	main()