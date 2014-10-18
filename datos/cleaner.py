#!/usr/bin/env python3

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

def procesarSujeto(sujeto):
	# obtenerRtrasCorrectasInmediato(sujeto)
	# obtenerRtas(sujeto, 6, 2)
	obtenerRtasCorrectasInmediatoBruto(sujeto)
	# if(esComputador(sujeto)):
		# obtenerRtas(sujeto, 6, 3)

def esComputador(sujeto):
	return sujeto['encuesta']['estudios'] == {'computacion': True}


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
	porcentaje = 0.0
	for rta in sujeto['inmediato']['respuestas']:
		indice, rta, tiempo = rta[0], rta[1], rta[2]
		if (secuencias_inmediato[indice]['largo'] == largo) and (secuencias_inmediato[indice]['depth'] == profundidad):
			if secuencias_inmediato[indice]['rta_correcta'] == rta:
				cant_rtas_correctas = cant_rtas_correctas + 1
	porcentaje = cant_rtas_correctas/6.0
	print cant_rtas_correctas 
	# print 'largo: ', largo 
	# print 'profundida: ', profundidad
	# print 'Porcentaje: ', porcentaje*100, '%'



def main():
	data = None
	with open('incc-tp1-export-16oct.json') as data_file:
		data = json.load(data_file)
	sujetos = OrderedDict(sorted(data['resultados'].items(), key=lambda t: t[0]))
	for key in sujetos:
		sujeto = sujetos[key]
		pprint(sujeto)
		procesarSujeto(sujeto)

if __name__ == '__main__':
	main()