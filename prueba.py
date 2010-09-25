#!/usr/bin/env python
#--coding: utf-8--

from materia import *
from os import sys

if len(sys.argv) == 1 or "-h" in sys.argv or "--help" in sys.argv:
	# Ayuda
	print "Muestra correlativas de materias"
	print "Uso:",sys.argv[0]," [materia]"
	print "donde [materia] puede ser un número, nombre o apodo"
	print "Ejemplos:"
	print sys.argv[0],"mate1"
	print sys.argv[0],"19"
	print sys.argv[0],"\"matemática 1\""
	sys.exit()

archivo = "materias.csv"
if "-f" in sys.argv or "--file" in sys.argv:
	# El usuario especificó un archivo de materias
	i = sys.argv.index("-f")
	archivo = sys.argv[i+1]
	del sys.argv[i:i+2]

m = materias(archivo)

if "-l" in sys.argv or "--list" in sys.argv:
	print "Lista de materias:"
	for n in m.mats:
		mat = m.mats[n]
		print "%2d %s\t%s" % (n,mat.nombre.ljust(27),"/".join(mat.apodo))
	sys.exit()

aprobadas = True # Listar correlativas aprobadas
if "-a" in sys.argv or "--aprobadas" in sys.argv:
	sys.argv.remove("-a")
	sys.argv.remove("--aprobadas")
	# Cargo la lista de aprobadas
	f = file("aprobadas.txt",'r')
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
	aprobadas = False

if "-t" in sys.argv or "--todas" in sys.argv:
	# Muestro todas las que puedo cursar
	for n in m.mats:
		materia = m.mats[n]
		c = m.correlativas(materia,aprobadas)
		if not materia.aprobada and not c:
			print materia.nombre
	sys.exit()

busqueda = sys.argv.pop()
materia = m.buscar(busqueda)

print "Correlativas para",materia.nombre,
if not aprobadas:
	print "(excluyendo aprobadas)"
else:
	print
for c in m.correlativas(materia,aprobadas):
	print c.nombre
