#!/usr/bin/python
# -*- coding: utf-8 -*-
def remove_repetidos(lista):
	clone=[]
	for c in lista:
		clone.append(c)
	print(clone)
	for i in range(0,len(lista)):
		print("i: %d" % i)
		for k in range(0,len(lista)):
			print("k: %d" % k)
			if lista[int(i)]==lista[int(k)]:
				del clone[int(i)]
	print(clone.sort())
	return clone.sort()

print(remove_repetidos([1,9,3,4,5,1]))
