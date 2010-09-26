#!/usr/bin/env python
#--coding: utf-8--

from materia import *
from os import sys
import argparse

parser = argparse.ArgumentParser(
		description='Información de materias y correlativas')
parser.add_argument('-f','--file',default='materias.csv',
		help='Carga la lista de materias de otro archivo')
parser.add_argument('-p','--passed-file',dest='pfile',default='aprobadas.txt',
		help='Carga la lista de materias aprobadas de otro archivo')
parser.add_argument('-l','--list', action='store_true',default=False,
		help='Mostrar la lista de materias')
parser.add_argument('-a','--available', action='store_true',default=False,
		help='Mostrar las materias que puedo cursar')
parser.add_argument('-x','--exclude-passed', action='store_true',default=False,
		dest='exclude', help='No mostrar materias ya aprobadas')
parser.add_argument('materia', nargs='*', default=[],
		help='Buscar correlativas de estas materias')
opciones = parser.parse_args()

m = materias(opciones.file)

# Cargo la lista de aprobadas
for linea in file(opciones.pfile,'r'):
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

if opciones.list:
	if opciones.exclude:
		print "Lista de materias por aprobar:"
	else:
		print "Lista de materias:"
	for n in m.mats:
		mat = m.mats[n]
		if mat.aprobada and opciones.exclude:
			continue
		print "%2d %s\t%s" % (n,mat.nombre.ljust(27),"/".join(mat.apodo))
	sys.exit()

if opciones.available:
	# Muestro todas las que puedo cursar
	for n in m.mats:
		materia = m.mats[n]
		c = m.correlativas(materia,False)
		if not materia.aprobada and not c:
			print materia.nombre
	sys.exit()

for busqueda in opciones.materia:
	try:
		materia = m.buscar(busqueda)
	except LookupError:
		print "-No encontré",busqueda
		continue
	print "-Correlativas para",materia.nombre,
	if opciones.exclude:
		print "(excluyendo aprobadas)"
	else:
		print
	correlativas = m.correlativas(materia,not opciones.exclude)
	if not correlativas:
		print "Ninguna"
		continue
	for c in correlativas:
		print c.nombre
