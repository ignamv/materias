#!/usr/bin/env python
#--coding: utf-8--

class materia():
	def __init__(self,nombre,apodo,horas,correlativas):
		self.nombre = nombre
		self.apodo = apodo
		self.horas = horas
		self.correlativas = correlativas
		self.aprobada = False

class materias():
	def __init__(self,archivo):
		""" Carga la lista de materias. Si el archivo es .pkl entonces viene
		incorporada la lista de materias aprobadas """
		if archivo[-4:] == ".csv":
			# Es un archivo separado por comas, importo
			import csv
			lector = csv.reader(open(archivo,'r'), delimiter=',')
			lector.next() # Me salteo la cabecera

			self.mats = {}
			for fila in lector:
				fila.reverse()
				n = int(fila.pop())
				nombre = fila.pop()
				apodos = fila.pop().strip().split(" ")
				if not apodos[0]:
					del apodos[0]
				apodos.append(nombre.lower())
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
				self.mats[n] = materia(nombre,apodos,horas,correlativas)
		else:
			# Cargo todo de una
			import pickle
			datos = open(archivo,'rb')
			self.mats = pickle.load(datos)

	def guardar(self,archivo):
		""" Crea un archivo .pkl con las materias 
		(ojo, guarda las aprobadas) """
		import pickle
		salida = open(archivo,'wb')
		pickle.dump(self.mats,salida)
		salida.close()

	def buscar(self, nombre):
		""" Busca entre las materias por número o apodo """
		nombre = nombre.lower()
		for n in self.mats:
			if nombre in self.mats[n].apodo or str(n) == nombre:
				return self.mats[n]
		raise LookupError

	def correlativas(self,materia,aprobadas=True,lista=None):
		""" Devuelve una lista de materias correlativas a materia.
		Si aprobadas es True, incluye las que ya fueron aprobadas,
		de lo contrario sólo lista las que falta aprobar
		"""
		# Todas las invocaciones hijo van a empezar con una lista cargada
		padre = False
		if lista is None:
			# Si mi lista está vacía, me llamó el usuario y tengo que devolver
			# algún valor más adelante
			lista = []
			padre = True
		if materia.aprobada and not aprobadas:
			# Salteo directamente
			return []
		for m in materia.correlativas:
			#TODO: que diferencie correl. de TP con final
			# Si ya está en la lista de correlativas no hace falta procesarla
			if m[0] not in lista:
				if aprobadas or not self.mats[m[0]].aprobada:
					lista.append(m[0])
					self.correlativas(self.mats[m[0]],aprobadas,lista)
		if padre:
			# Salida más linda
			lista.sort()
			return [self.mats[i] for i in lista]

