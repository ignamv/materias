#!/usr/bin/env python
#--coding: utf-8--

from materia import *

m = materias("materias.pkl")

from os import sys
busqueda = sys.argv.pop()
print "Correlativas para",busqueda
for c in m.correlativas(m.buscar(busqueda)):
	print c.nombre
#print m.buscar("m1").correlativas
