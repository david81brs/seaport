#!/usr/bin/python3
# -*- coding: utf-8 -*-

#rodadas	# - Conta o número de rodadas.
#n 			# - Registra o número de peças.
#m			# - Registra o limite de peças por jogada.

import time
import os

def sleepy():

	time.sleep(1)
	return

def computador_escolhe_jogada(n, m):

	while True:

		if (n-m) % (m+1) == 0:

			return m

		else:
			
			m=m-1
			return m


def usuario_escolhe_jogada(n,m):

	while n>0:

		m_user=int(input("Quantas peças você vai tirar? "))

		if m_user>m:

			print("Oops! Jogada inválida! Tente de novo.")

		else:
			return m_user
			break


def campeonato():

	rodada=1

	print("*** Rodada {} ***".format(rodada))
	print("Quantas peças?")
	n = int(input())
	print("Limite de peças por jogada? ")
	m = int(input())

	while rodada<=3:

		if (n-m) % (m+1) == 0:

			print("Computador começa!")

			while n!=0:

				vez="C"
				f=computador_escolhe_jogada(n,m)
				n=n-f
				print("Restam {} peças".format(n))

				if n==0 and vez=="C":
					print("Computador venceu")

				vez="U"
				u=usuario_escolhe_jogada(n,m)
				n=n-u
				if n==0 and vez=="U":

					print("Usuário venceu")

				print("Restam {} peças".format(n))
			print("Fim da rodada!")

		else:

			print("Você começa!")
			
			while n!=0:

				vez="U"
				u=usuario_escolhe_jogada(n,m)
				n=n-u
				print("Restam {} peças".format(n))
				
				if n==0 and vez=="U":
					print("Usuário venceu")
				
				vez="C"
				f=computador_escolhe_jogada(n,m)
				n=n-f
				
				if n==0 and vez=="C":
					print("Computador venceu")
				print("Restam {} peças".format(n))
			
			print("Fim da rodada!")

		rodada+=1

	print("Fim do campeonato!")

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

		print("Você escolheu um campeonato!")
		campeonato()

	elif choicy=='1':

		print("Você escolheu uma partida apenas.")
		partida()

	else:

		print("Você não escolheu nenhuma da opções.")

if __name__== '__main__':
	main()
