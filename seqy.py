#!/usr/bin/python
# -*- coding: utf-8 -*-

numby = []
while True:

	numa=int(input("Digite um número: "))
	if numa!=0:
		numby.append(numa)
	else:
		break
print("\n")
for nunc in range(len(numby)-1,-1,-1):
	print(numby[nunc])


