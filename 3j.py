#!/usr/bin/python3
# -*- coding: utf-8 -*-
# - Jogo Nim.py - 

def computador_escolhe_jogada(n, m):
	'''
		A função computador recebe o número de peças restantes e o limite 
		de cada jogada.
	'''
	pecas = n
	limit = m
	# print(n,m)
	resto = pecas - limit
	
		# Se retirar a quantidade limite significar deixar um resto divisível pelo limite + 1, que é a estratégia vencedora, enquanto ainda há peças, isto é, peças > 0, executar atribuíndo o retorno.
	

	if (resto % (limit+1)) == 0 and pecas>0:
		# print('a')
		escolhe=limit

		# Se não houver múltiplo, avaliar se a quantidade de peças restantes é inferior ao limite.
	

	elif pecas<=limit:
		# print('b')
		escolhe=pecas

	else:
		# print('c')
		escolhe=limit

	return escolhe


def usuario_escolhe_jogada(n,m):

	while n>0:

		print("\nQuantas peças você vai tirar safado? ", end="")
		m_user=int(input())

		if m_user>m or m_user<=0 or m_user>n:

			print("Oops! Jogada inválida! Tente de novo.")

		else:
			return m_user

# Essa função solicita os dados do usuário para cada partida.

def pedir():

	dados=[0,0]
	dados[0]=int(input("Quantas peças? "))
	dados[1]=int(input("Limite de peças por jogada? "))
	return dados

def campeonato():

	# Definir as variáveis do campeonato

	numero_max_rodadas=3
	rodada=1
	placar=[0,0]

	while rodada<=numero_max_rodadas:

		print("\n*** Rodada {} ***\n".format(rodada))
		
		dados=pedir()
		pecas=dados[0]
		limite=dados[1]
		resto=pecas

		vez=1 # usuário começa

		if (pecas % (limite+1)) == 0: # Se for multiplo o usuário começa
			print("\nVocê começa!\n")

		else:
			vez=0 # computador começa
			print("\nComputador começa!\n")

		county=1

		while resto>=1: 

		# Faz a interação de múltiplas jogadas enquanto o resto é maior ou igual à uma unidade.

			if county % 2 == 0: 
			# variável county faz a alternância da vez de cada agente.

				if vez==0:

					if resto!=0:
						jogada_computador=computador_escolhe_jogada(resto,limite)
						resto=resto-jogada_computador

					if jogada_computador==1:
						print("O computador tirou uma peça.")

					else:
						print("O computador tirou {} peças.".format(jogada_computador))
					
					if resto==1:
						print("Agora resta apenas uma peça no tabuleiro.\n")
					
					else:
						if resto!=0:
							print("Agora restam {} peças no tabuleiro.\n".format(resto))

					if resto==0:
						print("O computador ganhou!", end="")
						placar[0]=placar[0]+1

					vez=1

				else:

					if resto!=0:
						jogada_usuario=usuario_escolhe_jogada(resto,limite)
						resto=resto-jogada_usuario

					if jogada_usuario==1:
						print("Você tirou uma peça.")

					else:
						print("Você tirou {} peças.".format(jogada_usuario))

					if resto==1:
						print("Agora resta apenas uma peça.\n")

					else:
						if resto!=0:
							print("Agora restam {} peças no tabuleiro.\n".format(resto))

					if resto==0:
						print("Você venceu!",end="")
						placar[1]=placar[1]+1

					vez=0

			else:

				if vez==1:

					if resto!=0:
						jogada_usuario=usuario_escolhe_jogada(resto,limite)
						resto=resto-jogada_usuario

					if jogada_usuario==1:
						print("Você tirou uma peça.")

					else:
						print("Você tirou {} peças.".format(jogada_usuario))

					if resto==1:
						print("Agora resta apenas uma peça.\n")

					else:
						if resto!=0:
							print("Agora restam {} peças no tabuleiro.\n".format(resto))
					vez=0

					if resto==0:
						print("Você venceu!",end="")
						placar[1]=placar[1]+1
				else:

					if resto!=0:
						jogada_computador=computador_escolhe_jogada(resto,limite)
						resto=resto-jogada_computador

					if jogada_computador==1:
						print("O computador tirou uma peça.")

					else:
						print("O computador tirou {} peças.".format(jogada_computador))

					if resto==1:
						print("Agora resta apenas uma peça no tabuleiro.\n")

					else:
						if resto!=0:
							print("Agora restam {} peças no tabuleiro.\n".format(resto))

					if resto==0:
						print("O computador ganhou!", end="")
						placar[0]=placar[0]+1

					vez=1
			county+=1
			# resto-=1
		print("\n-------------------------------------")
		rodada+=1
	print("\n*** Final do campeonato! ***")
	print("\nPlacar: Você {}x{} Computador".format(placar[1],placar[0]))

campeonato()
# campeonato(3,6)