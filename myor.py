#!/usr/bin/python
# -*- coding: utf-8 -*-
def maior_elemento(lista):
	inicial=lista[0]
	resp=lista[0]
	for i in range(0,len(lista)-1):
		if lista[i]>inicial:
			resp = lista[i]
	return resp

print(maior_elemento([7,4,7,-1]))