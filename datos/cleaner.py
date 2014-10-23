#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from collections import OrderedDict
from pprint import pprint

secuencias_inmediato = [
	{'largo': 18, 'rta_correcta': 'N', 'depth':2},
	{'largo': 18, 'rta_correcta': 'N', 'depth':2},
	{'largo': 18, 'rta_correcta': 'S', 'depth':2},
	{'largo': 18, 'rta_correcta': 'N', 'depth':1},
	{'largo': 12, 'rta_correcta': 'N', 'depth':3},
	{'largo': 6, 'rta_correcta': 'N', 'depth':3},
	{'largo': 6, 'rta_correcta': 'S', 'depth':2},
	{'largo': 6, 'rta_correcta': 'S', 'depth':1},
	{'largo': 6, 'rta_correcta': 'N', 'depth':1},
	{'largo': 12, 'rta_correcta': 'S', 'depth':2},
	{'largo': 6, 'rta_correcta': 'N', 'depth':2},
	{'largo': 12, 'rta_correcta': 'N', 'depth':2},
	{'largo': 6, 'rta_correcta': 'N', 'depth':1},
	{'largo': 12, 'rta_correcta': 'S', 'depth':3},
	{'largo': 6, 'rta_correcta': 'S', 'depth':1},
	{'largo': 6, 'rta_correcta': 'N', 'depth':3},
	{'largo': 12, 'rta_correcta': 'N', 'depth':2},
	{'largo': 18, 'rta_correcta': 'S', 'depth':1},
	{'largo': 12, 'rta_correcta': 'S', 'depth':1},
	{'largo': 12, 'rta_correcta': 'S', 'depth':1},
	{'largo': 6, 'rta_correcta': 'S', 'depth':2},
	{'largo': 18, 'rta_correcta': 'N', 'depth':2},
	{'largo': 12, 'rta_correcta': 'S', 'depth':2},
	{'largo': 12, 'rta_correcta': 'N', 'depth':3},
	{'largo': 12, 'rta_correcta': 'N', 'depth':1},
	{'largo': 6, 'rta_correcta': 'N', 'depth':1},
	{'largo': 18, 'rta_correcta': 'N', 'depth':3},
	{'largo': 18, 'rta_correcta': 'S', 'depth':3},
	{'largo': 6, 'rta_correcta': 'S', 'depth':3},
	{'largo': 6, 'rta_correcta': 'N', 'depth':2},
	{'largo': 6, 'rta_correcta': 'N', 'depth':3},
	{'largo': 12, 'rta_correcta': 'N', 'depth':1},
	{'largo': 6, 'rta_correcta': 'S', 'depth':2},
	{'largo': 12, 'rta_correcta': 'N', 'depth':1},
	{'largo': 6, 'rta_correcta': 'S', 'depth':1},
	{'largo': 12, 'rta_correcta': 'S', 'depth':2},
	{'largo': 18, 'rta_correcta': 'N', 'depth':3},
	{'largo': 12, 'rta_correcta': 'N', 'depth':3},
	{'largo': 18, 'rta_correcta': 'N', 'depth':3},
	{'largo': 18, 'rta_correcta': 'S', 'depth':3},
	{'largo': 18, 'rta_correcta': 'S', 'depth':1},
	{'largo': 18, 'rta_correcta': 'N', 'depth':1},
	{'largo': 12, 'rta_correcta': 'S', 'depth':1},
	{'largo': 18, 'rta_correcta': 'S', 'depth':2},
	{'largo': 18, 'rta_correcta': 'S', 'depth':1},
	{'largo': 18, 'rta_correcta': 'S', 'depth':3},
	{'largo': 6, 'rta_correcta': 'S', 'depth':3},
	{'largo': 18, 'rta_correcta': 'N', 'depth':1},
	{'largo': 12, 'rta_correcta': 'N', 'depth':2},
	{'largo': 6, 'rta_correcta': 'S', 'depth':3},
	{'largo': 18, 'rta_correcta': 'S', 'depth':2},
	{'largo': 12, 'rta_correcta': 'S', 'depth':3},
	{'largo': 12, 'rta_correcta': 'S', 'depth':3},
	{'largo': 6, 'rta_correcta': 'N', 'depth':2}
]

secuencias_inconsciente = [
	{'largo': 18, 'rta_correcta': 'N', 'depth':2},
	{'largo': 18, 'rta_correcta': 'N', 'depth':1},
	{'largo': 18, 'rta_correcta': 'N', 'depth':1},
	{'largo': 18, 'rta_correcta': 'S', 'depth':2},
	{'largo': 18, 'rta_correcta': 'N', 'depth':1},
	{'largo': 18, 'rta_correcta': 'S', 'depth':3},
	{'largo': 18, 'rta_correcta': 'S', 'depth':1},
	{'largo': 18, 'rta_correcta': 'S', 'depth':1},
	{'largo': 18, 'rta_correcta': 'N', 'depth':3},
	{'largo': 18, 'rta_correcta': 'N', 'depth':2},
	{'largo': 18, 'rta_correcta': 'S', 'depth':1},
	{'largo': 18, 'rta_correcta': 'N', 'depth':3},
	{'largo': 18, 'rta_correcta': 'S', 'depth':3},
	{'largo': 18, 'rta_correcta': 'N', 'depth':2},
	{'largo': 18, 'rta_correcta': 'S', 'depth':2},
	{'largo': 18, 'rta_correcta': 'N', 'depth':3},
	{'largo': 18, 'rta_correcta': 'S', 'depth':3},
	{'largo': 18, 'rta_correcta': 'S', 'depth':2},
]


def procesarSujetosPorLargo(sujetos):
	# Analisis de baja de rendimiento según el largo
	for s in sujetos:	
		rtas_largo_6 = (0,0)
		rtas_largo_12 = (0,0)
		rtas_largo_18 = (0,0)
		for i in xrange(1,4):
			rtas_largo_6 = tuple(a+b for a,b in zip(rtas_largo_6, obtenerRtas(s, 6, i)))
			rtas_largo_12 = tuple(a+b for a,b in zip(rtas_largo_12, obtenerRtas(s, 12, i)))
			rtas_largo_18 = tuple(a+b for a,b in zip(rtas_largo_18, obtenerRtas(s, 18, i)))

		print(rtas_largo_6, rtas_largo_12, rtas_largo_18) 

def procesarSujetosPorProf(sujetos):
	# Analisis de baja de rendimiento según el largo
	for s in sujetos:	
		rtas_prof_1 = (0,0)
		rtas_prof_2 = (0,0)
		rtas_prof_3 = (0,0)
		for i in xrange(6,19, 6):
			rtas_prof_1 = tuple(a+b for a,b in zip(rtas_prof_1, obtenerRtas(s, i, 1)))
			rtas_prof_2 = tuple(a+b for a,b in zip(rtas_prof_2, obtenerRtas(s, i, 2)))
			rtas_prof_3 = tuple(a+b for a,b in zip(rtas_prof_3, obtenerRtas(s, i, 3)))

		print(rtas_prof_1, rtas_prof_2, rtas_prof_3) 

def procesarSujetosPorLargoYProf(sujetos):
	# Analisis de baja de rendimiento según el largo
	
	for i in xrange(6,19, 6):
		for j in xrange(1,4):
			print "Largo: ", i, "Prof: ", j
			for s in sujetos:	
				rtas = (0,0)
				rtas = obtenerRtas(s, i, j)
				print(rtas)

def procesarSujetosInconsciente(sujetos):
	for s in sujetos:	
		rtas_prof_1 = (0,0)
		rtas_prof_2 = (0,0)
		rtas_prof_3 = (0,0)

		rtas_prof_1 = obtenerRtasInc(s, 1)
		rtas_prof_2 = obtenerRtasInc(s, 2)	
		rtas_prof_3 = obtenerRtasInc(s, 3)
		print(rtas_prof_1, rtas_prof_2, rtas_prof_3) 

def procesarSujetosInconscientePorProf(sujetos):
	for i in xrange(1,4):
		print "Prof: ", i
		for s in sujetos:	
			rtas_prof= (0,0)
			rtas_prof = obtenerRtasInc(s, i)
			print(rtas_prof) 

def procesarSujeto(sujeto):
	# Analisis de baja de rendimiento según el largo
	


	# obtenerRtrasCorrectasInmediato(sujeto)
	# obtenerRtas(sujeto, 6, 2)

	# obtenerRtasCorrectasInmediatoBruto(sujeto)
	total = 0
	if(esComputador(sujeto)):
		for i in xrange(6,19,6):
			for j in xrange(1,4):
				# print "Computador largo: ", i, "Depth: ", j	
				total += obtenerRtas(sujeto, i, j)
		print total
		if total>=48:
			print "Una bestia"

def esComputador(sujeto):
	return sujeto['encuesta']['estudios'] == {'computacion': True}

def noEsComputador(sujeto):
	return not esComputador(sujeto)

def obtenerRtasCorrectasInmediato(sujeto):
	cant_rtas_correctas_inmediato = 0
	for rta_tiempo in sujeto['inmediato']['respuestas']:
		indice, rta, tiempo  = rta_tiempo[0], rta_tiempo[1], rta_tiempo[2]
		if secuencias_inmediato[indice]['rta_correcta'] == rta:
			cant_rtas_correctas_inmediato = cant_rtas_correctas_inmediato + 1
	print(cant_rtas_correctas_inmediato)

def obtenerRtasCorrectasInmediatoComp(sujeto):
	if(esComputador(sujeto)):
		cant_rtas_correctas_inmediato = 0
		for rta_tiempo in sujeto['inmediato']['respuestas']:
				indice, rta, tiempo  = rta_tiempo[0], rta_tiempo[1], rta_tiempo[2]
				if secuencias_inmediato[indice]['rta_correcta'] == rta:
					cant_rtas_correctas_inmediato = cant_rtas_correctas_inmediato + 1
		print(cant_rtas_correctas_inmediato)


def obtenerRtasCorrectasInmediatoBruto(sujeto):
	if(not esComputador(sujeto)):
		cant_rtas_correctas_inmediato = 0
		for rta_tiempo in sujeto['inmediato']['respuestas']:
				indice, rta, tiempo  = rta_tiempo[0], rta_tiempo[1], rta_tiempo[2]
				if secuencias_inmediato[indice]['rta_correcta'] == rta:
					cant_rtas_correctas_inmediato = cant_rtas_correctas_inmediato + 1
		print(cant_rtas_correctas_inmediato)


def obtenerRtas(sujeto, largo, profundidad):
	cant_rtas_correctas = 0
	t_total = 0
	porcentaje = 0.0
	for rta in sujeto['inmediato']['respuestas']:
		indice, rta, tiempo = rta[0], rta[1], rta[2]
		if (secuencias_inmediato[indice]['largo'] == largo) and (secuencias_inmediato[indice]['depth'] == profundidad):
			t_total += tiempo
			if secuencias_inmediato[indice]['rta_correcta'] == rta:
				cant_rtas_correctas = cant_rtas_correctas + 1
	return cant_rtas_correctas, t_total
	# print 'largo: ', largo 
	# print 'profundida: ', profundidad
	# print 'Porcentaje: ', porcentaje*100, '%'

def obtenerRtasInc(sujeto, profundidad):
	cant_rtas_correctas = 0
	t_total = 0
	porcentaje = 0.0
	for rta in sujeto['inconsciente']['respuestas']:
		indice, rta, tiempo = rta[0], rta[1], rta[2]
		if (secuencias_inconsciente[indice]['depth'] == profundidad):
			t_total += tiempo
			if secuencias_inconsciente[indice]['rta_correcta'] == rta:
				cant_rtas_correctas = cant_rtas_correctas + 1
	return cant_rtas_correctas, t_total



def main():
	data = None
	with open('incc-tp1-export-16oct.json') as data_file:
		data = json.load(data_file)
	sujetos = OrderedDict(sorted(data['resultados'].items(), key=lambda t: t[0]))
	# print sujetos.keys()
	values = sujetos.values()

	# Analisis de baja de rendimiento según el largo
	print "Total sujetos en largos 6, 12, 18 (Rtas Correctas, Tiempo Total)"
	procesarSujetosPorLargo(values)

	print "\n"

	# Analisis de baja de rendimiento según el largo Comp
	print "Computadores en largos 6, 12, 18 (Rtas Correctas, Tiempo Total)"
	procesarSujetosPorLargo(filter(esComputador, values))

	print "\n"

	# Analisis de baja de rendimiento según el largo No Comp
	print "No computadores en largos 6, 12, 18 (Rtas Correctas, Tiempo Total)"
	procesarSujetosPorLargo(filter(noEsComputador, values))

	print "\n"

	# Analisis de baja de rendimiento según el profundidad
	print "Total sujetos en prof 1, 2, 3 (Rtas Correctas, Tiempo Total)"
	procesarSujetosPorProf(values)

	print "\n"

	# Analisis de baja de rendimiento según el largo Comp
	print "Computadores en prof 1, 2, 3 (Rtas Correctas, Tiempo Total)"
	procesarSujetosPorProf(filter(esComputador, values))

	print "\n"

	# Analisis de baja de rendimiento según el largo No Comp
	print "No computadores prof 1, 2, 3 (Rtas Correctas, Tiempo Total)"
	procesarSujetosPorProf(filter(noEsComputador, values))

	print "\n"

	# Analisis por largo y prof total sujetos
	print "Total sujetos largo 6,12,18 y prof 1, 2, 3 (Rtas Correctas, Tiempo Total)"
	procesarSujetosPorLargoYProf(values)

	print "\n"

	# Analisis por largo y prof total computadores
	print "Computadores largo 6,12,18 y prof 1, 2, 3 (Rtas Correctas, Tiempo Total)"
	procesarSujetosPorLargoYProf(filter(esComputador,values))

	print "\n"

	# Analisis por largo y prof No Computadores
	print "No Computadores largo 6,12,18 y prof 1, 2, 3 (Rtas Correctas, Tiempo Total)"
	procesarSujetosPorLargoYProf(filter(noEsComputador, values))

	print "\n"

	# Analisis total sujetos INCONSCIENTE
	print "Total Sujetos INCONSCIENTE (Rtas Correctas, Tiempo Total)"
	procesarSujetosInconsciente(values)

	print "\n"

	# Analisis Computadores INCONSCIENTE
	print "Computadores INCONSCIENTE (Rtas Correctas, Tiempo Total)"
	procesarSujetosInconsciente(filter(esComputador,values))

	print "\n"

	# Analisis No Computadores INCONSCIENTE
	print "No Computadores INCONSCIENTE (Rtas Correctas, Tiempo Total)"
	procesarSujetosInconsciente(filter(noEsComputador,values))

	print "\n"

	# Analisis total sujetos por prof INCONSCIENTE
	print "Total sujetos por prof INCONSCIENTE (Rtas Correctas, Tiempo Total)"
	procesarSujetosInconscientePorProf(values)

	print "\n"

	# Analisis Computadores por prof INCONSCIENTE
	print "Computadores por prof INCONSCIENTE (Rtas Correctas, Tiempo Total)"
	procesarSujetosInconscientePorProf(filter(esComputador, values))

	print "\n"

	# Analisis Computadores por prof INCONSCIENTE
	print "No Computadores por prof INCONSCIENTE (Rtas Correctas, Tiempo Total)"
	procesarSujetosInconscientePorProf(filter(noEsComputador, values))

	print "\n"


if __name__ == '__main__':
	main()