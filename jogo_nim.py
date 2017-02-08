
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

# def computador_escolhe_jogada(n, m):
# 	'''
# 		A função computador recebe o número de peças restantes e o limite 
# 		de cada jogada.
# 	'''
# 	pecas = n
# 	limit = m
# 	# print(n,m)
# 	resto = pecas // limit
	
# 		# Se retirar a quantidade limite significar deixar um resto divisível pelo limite + 1, que é a estratégia vencedora, enquanto ainda há peças, isto é, peças > 0, executar atribuíndo o retorno.
	

# 	if (resto % (limit+1)) == 0 and pecas>0:
# 		# print('a')
# 		escolhe=limit

# 		# Se não houver múltiplo, avaliar se a quantidade de peças restantes é inferior ao limite.
	

# 	elif pecas<=limit:
# 		# print('b')
# 		escolhe=pecas

# 	else:
# 		# print('c')
# 		escolhe=limit

# 	return escolhe
def computador_escolhe_jogada(pecas,jogada_maxima):
    escolha = 0
    if jogada_maxima>=1 and jogada_maxima <=pecas:
        
        for jogada_teste in range(jogada_maxima,0,-1):
            resto = pecas % jogada_teste
            # print('pecas %d jt: %d resto: %d jm: %d multiplo (%d+1): %d ' 
                # % (pecas, jogada_teste, resto, jogada_maxima, jogada_maxima,resto/(jogada_maxima+1)))
            if (pecas - jogada_teste) % (jogada_maxima+1) == 0 :
                escolha = jogada_teste
            else:
                escolha = jogada_maxima
    else:
        escolha = pecas

    return escolha


def usuario_escolhe_jogada(n,m):

	while n>0:

		print("\nQuantas peças você vai tirar? ", end="")
		m_user=int(input())

		if m_user>m or m_user<=0 or m_user>n:

			print("Oops! Jogada inválida! Tente de novo.")

		else:
			return m_user


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

# def partida():

# 	print("\nQuantas peças? ", end="")
# 	pecas = int(input())
# 	print("Limite de peças por jogada? ", end="")
# 	limite = int(input())
# 	resto=pecas-limite

# 	vez=1 # usuário começa

# 	if (pecas % (limite+1)) == 0: # Se for multiplo o usuário começa
# 		print("\nVocê começa!\n")

# 	else:
# 		vez=0 # computador começa
# 		print("\nComputador começa!\n")

# 	county=1

# 	while resto>=1: 

# 		# Faz a interação de múltiplas jogadas enquanto o resto é maior ou igual à uma unidade.

# 			if county % 2 == 0: 
# 			# variável county faz a alternância da vez de cada agente.

# 				if vez==0:

# 					if resto!=0:
# 						jogada_computador=computador_escolhe_jogada(resto,limite)
# 						resto=resto-jogada_computador

# 					if jogada_computador==1:
# 						print("O computador tirou uma peça.")

# 					else:
# 						print("O computador tirou {} peças.".format(jogada_computador))
					
# 					if resto==1:
# 						print("Agora resta apenas uma peça no tabuleiro.\n")
					
# 					else:
# 						if resto!=0:
# 							print("Agora restam {} peças no tabuleiro.\n".format(resto))

# 					if resto==0:
# 						print("O computador ganhou!", end="")
						
# 					vez=1

# 				else:

# 					if resto!=0:
# 						jogada_usuario=usuario_escolhe_jogada(resto,limite)
# 						resto=resto-jogada_usuario

# 					if jogada_usuario==1:
# 						print("Você tirou uma peça.")

# 					else:
# 						print("Você tirou {} peças.".format(jogada_usuario))

# 					if resto==1:
# 						print("Agora resta apenas uma peça.\n")

# 					else:
# 						if resto!=0:
# 							print("Agora restam {} peças no tabuleiro.\n".format(resto))

# 					if resto==0:
# 						print("Você venceu!",end="")

# 					vez=0

# 			else:

# 				if vez==1:

# 					if resto!=0:
# 						jogada_usuario=usuario_escolhe_jogada(resto,limite)
# 						resto=resto-jogada_usuario

# 					if jogada_usuario==1:
# 						print("Você tirou uma peça.")

# 					else:
# 						print("Você tirou {} peças.".format(jogada_usuario))

# 					if resto==1:
# 						print("Agora resta apenas uma peça.\n")

# 					else:
# 						if resto!=0:
# 							print("Agora restam {} peças no tabuleiro.\n".format(resto))
# 					vez=0

# 					if resto==0:
# 						print("Você venceu!",end="")

# 				else:

# 					if resto!=0:
# 						jogada_computador=computador_escolhe_jogada(resto,limite)
# 						resto=resto-jogada_computador

# 					if jogada_computador==1:
# 						print("O computador tirou uma peça.")

# 					else:
# 						print("O computador tirou {} peças.".format(jogada_computador))

# 					if resto==1:
# 						print("Agora resta apenas uma peça no tabuleiro.\n")

# 					else:
# 						if resto!=0:
# 							print("Agora restam {} peças no tabuleiro.\n".format(resto))

# 					if resto==0:
# 						print("O computador ganhou!", end="")

# 					vez=1
# 			county+=1
# 	print("Fim de jogo!")
def partida():

	# Definir as variáveis do campeonato

	numero_max_rodadas=1
	
	placar=[0,0]

	

		# print("\n*** Rodada {} ***\n".format(rodada))
		
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
					print("Fim do Jogo! O computador ganhou!")
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
					print("Fim do jogo! Você venceu!")
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
					print("Fim do Jogo! Você venceu!")
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
					print("Fim do jogo! O computador ganhou!")
					placar[0]=placar[0]+1

				vez=1
		county+=1
		

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
