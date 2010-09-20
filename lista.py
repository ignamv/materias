#!/usr/bin/env python

import csv
from materia import materia

lector = csv.reader(open("materias.csv",'r'), delimiter=',')
lector.next() # Me salteo la cabecera

mats = {}
for fila in lector:
	fila.reverse()
	n = int(fila.pop())
	nombre = fila.pop()
	apodos = fila.pop().split(" ")
	horas = tuple(fila[-3:])
	del fila[-3:]
	correlativas = []
	for corr in fila.pop().split(" "):
		if not corr:
			break
		tp = False
		if corr.find("(TP)") != -1:
			corr = corr.replace("(TP)","")
			tp = True
		ncorr = int(corr)
		correlativas.append((ncorr,tp))
	mats[n] = materia(nombre,apodos,horas,correlativas)

import pickle
salida = open("materias.pkl",'wb')
pickle.dump(mats,salida)
salida.close()
