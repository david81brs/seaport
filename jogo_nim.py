#!/usr/bin/python3
# -*- coding: utf-8 -*-

#rodadas	# - Conta o número de rodadas.
#n 			# - Registra o número de peças.
#m			# - Registra o limite de peças por jogada.

import time
import os

def sleepy():

	time.sleep(0)
	return

def computador_escolhe_jogada(n, m):

    comput=1
    jogcp=True
    while comput<m and jogcp:
	    if ((n-comput) % (m+1)) == 0:
		    jogcp=False
	    else:
	        comput+=1
	    return comput

def usuario_escolhe_jogada(n,m):

	while n>0:

		print("Quantas peças você vai tirar? ", end="")
		m_user=int(input())

		if m_user>m or m_user<=0:

			print("Oops! Jogada inválida! Tente de novo.")

		else:
			return m_user
			break


def campeonato():

	rodada=1
	placar=[0,0]

	while rodada<=3:

		print("\n*** Rodada {} ***\n".format(rodada))
		print("Quantas peças? ", end="")
		n = int(input())
		print("Limite de peças por jogada? ", end="")
		m = int(input())

		if (n-m) % (m+1) == 0:

			print("\nComputador começa!\n")

			while n>=0:

				#sleepy()


				if n>=0:
					f=computador_escolhe_jogada(n,m)
					try:
						n=n-f
						vez="C"
						if f==1:
							print("O computador tirou uma peça.")
						else:
							print("O computador tirou {} peças.".format(f))
						if n==1:
							print("Agora resta apenas uma peça no tabuleiro.\n")
						else:
							if n!=0:
								print("Agora restam {} peças no tabuleiro.\n".format(n))
					except:
						n=0
						break

				if n>=0:
					u=usuario_escolhe_jogada(n,m)
					try:
						n=n-u
						vez="U"
						if u==1:
							print("Você tirou uma peça.")
						else:
							print("Você tirou {} peças.".format(u))
						if n==1:
							print("Agora resta apenas uma peça.\n")
						else:
							if n!=0:
								print("Agora restam {} peças no tabuleiro.\n".format(n))
					except:
						n=0
						break

			if n==0 and vez=="C":
						print("O computador ganhou!", end="")
						placar[0]=placar[0]+1

			if n==0 and vez=="U":
						print("Usuário venceu!", end="")
						placar[1]=placar[1]+1

			print(" Fim de jogo!")

		else:

			print("\nVocê começa!\n")

			while n>=0:

				if n>=0:
					try:
					    u=usuario_escolhe_jogada(n,m)
					    n=n-u
					    vez="U"
					    if u==1:
					        print("Você tirou uma peça.")
					    else:
					        print("Você tirou {} peças.".format(u)
				        if n==1:
				            print("Agora resta apenas uma peça.\n")
				        else:
				            if n!=0:
				                print("Agora restam {} peças no tabuleiro\n".format(n))
				    except:
				        n=0
				        break

				#sleepy()

				if n>=0:
					try:
					    f=computador_escolhe_jogada(n,m)
						n=n-f
						vez="C"
						if f==0:
							print("O computador tirou uma peça.")
						else:
							print("O computador tirou {} peças.".format(f))
						if n==1:
							print("Agora resta apenas uma peça.\n")
						else:
							if n!=0:
								print("Agora restam {} peças no tabuleiro.\n".format(n))
					except:
						n=0
						break

			if n==0 and vez=="C":
						print("O computador ganhou!", end="")
						placar[0]=placar[0]+1

			if n==0 and vez=="U":
						print("Usuário venceu!",end="")
						placar[1]=placar[1]+1

			print(" Fim do jogo!".format(rodada))

		rodada+=1

	print("\n*** Final do campeonato! ***")
	print("\nPlacar: Você {}x{} Computador".format(placar[1],placar[0]))

def partida():

	print("Quantas peças?")
	n = int(input())
	print("Limite de peças por jogada? ")
	m = int(input())

	if (n-m) % (m+1) == 0:

		print("Computador começa!")

		while n>=0:

			sleepy()

			if n>=0:
				f=computador_escolhe_jogada(n,m)
				try:
					n=n-f
					vez="C"
					print("O computador tirou {}".format(f))
					print("Restam {} peças".format(n))
				except:
					n=0
					break

			if n>=0:
				u=usuario_escolhe_jogada(n,m)
				try:
					n=n-u
					vez="U"
					print("Você tirou {}".format(u))
					print("Restam {} peças".format(n))
				except:
					n=0
					break

		if n==0 and vez=="C":
					print("Computador venceu!")

		if n==0 and vez=="U":
					print("Usuário venceu!")

		print("Fim de jogo!")

	else:

		print("Você começa!")

		while n!=0:

			u=usuario_escolhe_jogada(n,m)
			n=n-u

			if n>=0:

				vez="U"
				print("Você tirou {}".format(u))
				print("Restam {} peças".format(n))

			sleepy()

			f=computador_escolhe_jogada(n,m)
			n=n-f

			if n>=0:

				vez="C"
				print("O computador tirou {}".format(f))
				print("Restam {} peças".format(n))

		if n==0 and vez=="C":
					print("Computador venceu!")
		if n==0 and vez=="U":
					print("Usuário venceu!")

		print("Fim de jogo!")

def main():

	os.system("clear")

	print("Bem-vindo ao jogo do NIM! Escolha:")
	print("1 - para jogar uma partida isolada")
	print("2 - para jogar um campeonato", end=" ")

	choicy = input()

	if choicy=='2':

		print("\nVocê escolheu um campeonato!")
		campeonato()

	elif choicy=='1':

		print("\nVocê escolheu uma partida apenas.")
		partida()

	else:

		print("\nVocê não escolheu nenhuma da opções.")

if __name__== '__main__':
	main()
