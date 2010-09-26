#!/usr/bin/env python
#--coding: utf-8--

from materia import *
from os import sys
import argparse

parser = argparse.ArgumentParser(
	description='Información de materias y correlativas')
parser.add_argument('-f','--file',default='materias.csv')
parser.add_argument('-p','--passed-file',dest='pfile',default='aprobadas.txt')
parser.add_argument('-l','--list', action='store_true',default=False)
parser.add_argument('-a','--available', action='store_true',default=False)
parser.add_argument('-x','--exclude-passed', action='store_true',default=False,
		dest='exclude')
parser.add_argument('materia', nargs='+')
opciones = parser.parse_args()

m = materias(opciones.file)

if opciones.list:
	print "Lista de materias:"
	for n in m.mats:
		mat = m.mats[n]
		print "%2d %s\t%s" % (n,mat.nombre.ljust(27),"/".join(mat.apodo))
	sys.exit()

# Cargo la lista de aprobadas
f = file(opciones.pfile,'r')
for linea in f:
	linea = linea.strip()
	if not linea:
		continue
	try:
		materia = m.buscar(linea)
	except LookupError:
		# Los ignoro...
		print "Materia no reconocida:",linea
		print type(linea)
		continue
	materia.aprobada = True

if opciones.available:
	# Muestro todas las que puedo cursar
	for n in m.mats:
		materia = m.mats[n]
		c = m.correlativas(materia,not opciones.exclude)
		if not materia.aprobada and not c:
			print materia.nombre
	sys.exit()

for busqueda in opciones.materia:
	materia = m.buscar(busqueda)
	print "Correlativas para",materia.nombre,
	if opciones.exclude:
		print "(excluyendo aprobadas)"
	else:
		print
	for c in m.correlativas(materia,not opciones.exclude):
		print c.nombre
