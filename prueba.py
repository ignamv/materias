#!/usr/bin/env python
#--coding: utf-8--

from materia import *

m = materias("materias.csv")
aprobadas = True # Listar correlativas aprobadas

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
elif "-l" in sys.argv or "--list" in sys.argv:
	print "Lista de materias:"
	for n in m.mats:
		mat = m.mats[n]
		print "%2d %s\t%s" % (n,mat.nombre.ljust(27),"/".join(mat.apodo))
	sys.exit()
elif "-a" in sys.argv or "--aprobadas" in sys.argv:
	# No listo correlativas que ya aprobé
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

busqueda = sys.argv.pop()
materia = m.buscar(busqueda)

print "Correlativas para",materia.nombre,
if not aprobadas:
	print "(excluyendo aprobadas)"
else:
	print
for c in m.correlativas(materia,aprobadas):
	print c.nombre
