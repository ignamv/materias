#!/usr/bin/env python
#--coding: utf-8--

from materia import *

m = materias("materias.csv")

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
elif "-a" in sys.argv or "--available" in sys.argv:
	# TODO: implementar un archivo con materias aprobadas
	print "Materias que se pueden cursar"
	print "Proximamente"

busqueda = sys.argv.pop()
materia = m.buscar(busqueda)

print "Correlativas para",materia.nombre
for c in m.correlativas(materia):
	print c.nombre
