#!/usr/bin/env python
#--coding: utf-8--

import pickle
from materia import materia

hechas = range(7)
# sarasa

def arbolito(lista):
	for m in lista:
		#TODO: que diferencie correl. de TP con final
		if m[0] not in todas and m[0] not in hechas:
			todas.append(m[0])
			arbolito(mats[m[0]].correlativas)

datos = open('materias.pkl','rb')
mats = pickle.load(datos)

from os import sys
if len(sys.argv) == 1:
	print "Uso:",sys.argv[0]," [n materia]"
	for n in mats:
		print "%3d %s\t%s" % (n,mats[n].nombre.ljust(30),
				" ".join(mats[n].apodo))
	sys.exit()

# Me fijo qué materia quiere (quizás usó un apodo)
pedido = sys.argv.pop()
encontrada = False
for n in mats:
	if pedido in mats[n].apodo or str(n) == pedido:
		encontrada = True
		break
if not encontrada:
	print "No encontré la materia"
	sys.exit()

mat = mats[n]
print "Correlativas para",mat.nombre,"o quizás","/".join(mat.apodo)
todas = []
arbolito(mat.correlativas)
todas.sort()
for n in todas:
	print n,mats[n].nombre
