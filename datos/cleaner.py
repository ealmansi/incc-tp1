#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from collections import OrderedDict
from pprint import pprint

secuencias_inmediato = [
	{'largo': 18, 'respuesta': 'N', 'prof':2},
	{'largo': 18, 'respuesta': 'N', 'prof':2},
	{'largo': 18, 'respuesta': 'S', 'prof':2},
	{'largo': 18, 'respuesta': 'N', 'prof':1},
	{'largo': 12, 'respuesta': 'N', 'prof':3},
	{'largo': 6, 'respuesta': 'N', 'prof':3},
	{'largo': 6, 'respuesta': 'S', 'prof':2},
	{'largo': 6, 'respuesta': 'S', 'prof':1},
	{'largo': 6, 'respuesta': 'N', 'prof':1},
	{'largo': 12, 'respuesta': 'S', 'prof':2},
	{'largo': 6, 'respuesta': 'N', 'prof':2},
	{'largo': 12, 'respuesta': 'N', 'prof':2},
	{'largo': 6, 'respuesta': 'N', 'prof':1},
	{'largo': 12, 'respuesta': 'S', 'prof':3},
	{'largo': 6, 'respuesta': 'S', 'prof':1},
	{'largo': 6, 'respuesta': 'N', 'prof':3},
	{'largo': 12, 'respuesta': 'N', 'prof':2},
	{'largo': 18, 'respuesta': 'S', 'prof':1},
	{'largo': 12, 'respuesta': 'S', 'prof':1},
	{'largo': 12, 'respuesta': 'S', 'prof':1},
	{'largo': 6, 'respuesta': 'S', 'prof':2},
	{'largo': 18, 'respuesta': 'N', 'prof':2},
	{'largo': 12, 'respuesta': 'S', 'prof':2},
	{'largo': 12, 'respuesta': 'N', 'prof':3},
	{'largo': 12, 'respuesta': 'N', 'prof':1},
	{'largo': 6, 'respuesta': 'N', 'prof':1},
	{'largo': 18, 'respuesta': 'N', 'prof':3},
	{'largo': 18, 'respuesta': 'S', 'prof':3},
	{'largo': 6, 'respuesta': 'S', 'prof':3},
	{'largo': 6, 'respuesta': 'N', 'prof':2},
	{'largo': 6, 'respuesta': 'N', 'prof':3},
	{'largo': 12, 'respuesta': 'N', 'prof':1},
	{'largo': 6, 'respuesta': 'S', 'prof':2},
	{'largo': 12, 'respuesta': 'N', 'prof':1},
	{'largo': 6, 'respuesta': 'S', 'prof':1},
	{'largo': 12, 'respuesta': 'S', 'prof':2},
	{'largo': 18, 'respuesta': 'N', 'prof':3},
	{'largo': 12, 'respuesta': 'N', 'prof':3},
	{'largo': 18, 'respuesta': 'N', 'prof':3},
	{'largo': 18, 'respuesta': 'S', 'prof':3},
	{'largo': 18, 'respuesta': 'S', 'prof':1},
	{'largo': 18, 'respuesta': 'N', 'prof':1},
	{'largo': 12, 'respuesta': 'S', 'prof':1},
	{'largo': 18, 'respuesta': 'S', 'prof':2},
	{'largo': 18, 'respuesta': 'S', 'prof':1},
	{'largo': 18, 'respuesta': 'S', 'prof':3},
	{'largo': 6, 'respuesta': 'S', 'prof':3},
	{'largo': 18, 'respuesta': 'N', 'prof':1},
	{'largo': 12, 'respuesta': 'N', 'prof':2},
	{'largo': 6, 'respuesta': 'S', 'prof':3},
	{'largo': 18, 'respuesta': 'S', 'prof':2},
	{'largo': 12, 'respuesta': 'S', 'prof':3},
	{'largo': 12, 'respuesta': 'S', 'prof':3},
	{'largo': 6, 'respuesta': 'N', 'prof':2}
]

secuencias_inconsciente = [
	{'largo': 18, 'respuesta': 'N', 'prof':2},
	{'largo': 18, 'respuesta': 'N', 'prof':1},
	{'largo': 18, 'respuesta': 'N', 'prof':1},
	{'largo': 18, 'respuesta': 'S', 'prof':2},
	{'largo': 18, 'respuesta': 'N', 'prof':1},
	{'largo': 18, 'respuesta': 'S', 'prof':3},
	{'largo': 18, 'respuesta': 'S', 'prof':1},
	{'largo': 18, 'respuesta': 'S', 'prof':1},
	{'largo': 18, 'respuesta': 'N', 'prof':3},
	{'largo': 18, 'respuesta': 'N', 'prof':2},
	{'largo': 18, 'respuesta': 'S', 'prof':1},
	{'largo': 18, 'respuesta': 'N', 'prof':3},
	{'largo': 18, 'respuesta': 'S', 'prof':3},
	{'largo': 18, 'respuesta': 'N', 'prof':2},
	{'largo': 18, 'respuesta': 'S', 'prof':2},
	{'largo': 18, 'respuesta': 'N', 'prof':3},
	{'largo': 18, 'respuesta': 'S', 'prof':3},
	{'largo': 18, 'respuesta': 'S', 'prof':2},
]

profundidades = [1, 2, 3]
largos = [6, 12, 18]

def imprimirEncabezado():
	print("Computador", end=";")
	print("PcjAciertosTotal", end=";")
	print("PcjAciertosProf1", end=";")
	print("PcjAciertosProf2", end=";")
	print("PcjAciertosProf3", end=";")
	print("PcjAciertosLargo6", end=";")
	print("PcjAciertosLargo12", end=";")
	print("PcjAciertosLargo18", end=";")
	print("TPromTotal", end=";")
	print("TPromProf1", end=";")
	print("TPromProf2", end=";")
	print("TPromProf3", end=";")
	print("TPromLargo6", end=";")
	print("TPromLargo12", end=";")
	print("TPromLargo18", end=";")
	print()

def imprimirEsComputador(sujeto):
	if ('computacion' in sujeto['encuesta']['estudios']
		and sujeto['encuesta']['estudios']['computacion']):
		print(1, end=";")
	else:
		print(0, end=";")

def imprimirInmPcjAciertosTotal(sujeto):
	cantRespuestasCorrectas = 0
	for respuesta in sujeto['inmediato']['respuestas']:
		indice, respuesta, tiempo = respuesta[0], respuesta[1], respuesta[2]
		if secuencias_inmediato[indice]['respuesta'] == respuesta:
			cantRespuestasCorrectas += 1
	porcentaje = float(cantRespuestasCorrectas) / len(sujeto['inmediato']['respuestas'])
	print(round(porcentaje, 4), end=";")

def imprimirInmPcjAciertosPorProf(sujeto):
	cantRespuestasCorrectasPorProf = {p:0 for p in profundidades}
	cantRespuestasPorProf = {p:0 for p in profundidades}
	for respuesta in sujeto['inmediato']['respuestas']:
		indice, respuesta, tiempo = respuesta[0], respuesta[1], respuesta[2]
		if secuencias_inmediato[indice]['respuesta'] == respuesta:
			cantRespuestasCorrectasPorProf[secuencias_inmediato[indice]['prof']] += 1
		cantRespuestasPorProf[secuencias_inmediato[indice]['prof']] += 1
	for p in profundidades:
		porcentaje = float(cantRespuestasCorrectasPorProf[p]) / cantRespuestasPorProf[p]
		print(round(porcentaje, 4), end=";")

def imprimirInmPcjAciertosPorLargo(sujeto):
	cantRespuestasCorrectasPorLargo = {l:0 for l in largos}
	cantRespuestasPorLargo = {l:0 for l in largos}
	for respuesta in sujeto['inmediato']['respuestas']:
		indice, respuesta, tiempo = respuesta[0], respuesta[1], respuesta[2]
		if secuencias_inmediato[indice]['respuesta'] == respuesta:
			cantRespuestasCorrectasPorLargo[secuencias_inmediato[indice]['largo']] += 1
		cantRespuestasPorLargo[secuencias_inmediato[indice]['largo']] += 1
	for l in largos:
		porcentaje = float(cantRespuestasCorrectasPorLargo[l]) / cantRespuestasPorLargo[l]
		print(round(porcentaje, 4), end=";")

def imprimirInmTPromTotal(sujeto):
	tAcum = 0
	for respuesta in sujeto['inmediato']['respuestas']:
		indice, respuesta, tiempo = respuesta[0], respuesta[1], respuesta[2]
		tAcum += tiempo
	tProm = float(tAcum) / len(sujeto['inmediato']['respuestas'])
	print(round(tProm, 4), end=";")

def imprimirInmTPromPorProf(sujeto):
	tAcumPorProf = {p:0 for p in profundidades}
	cantRespuestasPorProf = {p:0 for p in profundidades}
	for respuesta in sujeto['inmediato']['respuestas']:
		indice, respuesta, tiempo = respuesta[0], respuesta[1], respuesta[2]
		tAcumPorProf[secuencias_inmediato[indice]['prof']] += tiempo
		cantRespuestasPorProf[secuencias_inmediato[indice]['prof']] += 1
	for p in profundidades:
		tProm = float(tAcumPorProf[p]) / cantRespuestasPorProf[p]
		print(round(tProm, 4), end=";")

def imprimirInmTPromPorLargo(sujeto):
	tAcumPorLargo = {l:0 for l in largos}
	cantRespuestasPorLargo = {l:0 for l in largos}
	for respuesta in sujeto['inmediato']['respuestas']:
		indice, respuesta, tiempo = respuesta[0], respuesta[1], respuesta[2]
		tAcumPorLargo[secuencias_inmediato[indice]['largo']] += tiempo
		cantRespuestasPorLargo[secuencias_inmediato[indice]['largo']] += 1
	for l in largos:
		tProm = float(tAcumPorLargo[l]) / cantRespuestasPorLargo[l]
		print(round(tProm, 4), end=";")

def imprimirIncPcjAciertosTotal(sujeto):
	pass

def imprimirIncPcjAciertosPorProf(sujeto):
	pass

def imprimirIncTPromTotal(sujeto):
	pass

def imprimirIncTPromPorProf(sujeto):
	pass

def procesarSujeto(sujeto):
	imprimirEsComputador(sujeto)
	imprimirInmPcjAciertosTotal(sujeto)
	imprimirInmPcjAciertosPorProf(sujeto)
	imprimirInmPcjAciertosPorLargo(sujeto)
	imprimirInmTPromTotal(sujeto)
	imprimirInmTPromPorProf(sujeto)
	imprimirInmTPromPorLargo(sujeto)
	imprimirIncPcjAciertosTotal(sujeto)
	imprimirIncPcjAciertosPorProf(sujeto)
	imprimirIncTPromTotal(sujeto)
	imprimirIncTPromPorProf(sujeto)
	print()

def main():
	data = None
	with open('incc-tp1-export-16oct.json') as data_file:
		data = json.load(data_file)
	sujetos = OrderedDict(sorted(data['resultados'].items(), key=lambda t: t[0]))

	imprimirEncabezado()
	for sujeto in sujetos.values():
		procesarSujeto(sujeto)

if __name__ == '__main__':
	main()