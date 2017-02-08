#!/usr/bin/python
# -*- coding: utf-8 -*-
def soma_elementos(listy):
	acu=0
	for i in listy:
		acu=acu+int(i)
		#print(acu)
	return acu

#print(soma_elementos([1,2,3,4]))