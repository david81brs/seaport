#!/usr/bin/python3
# -*- coding: utf-8 -*-

def computador_escolhe_jogada(n, m):

		if (n-m) % (m+1) == 0:
			return m
		else:
			return m


def usuario_escolhe_jogada(n,m):

	while n>0:

		print("Quantas peças você vai tirar? ", end="")
		m_user=int(input())

		if m_user>m or m_user>n:

			print("Oops! Jogada inválida! Tente de novo.")

		else:
			return m_user
			break


