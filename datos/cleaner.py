#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from collections import OrderedDict
from pprint import pprint

profundidades = [1, 2, 3]
largos = [6, 12, 18]
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

def main():
	data = None
	with open('incc-tp1-export-16oct.json') as data_file:
		data = json.load(data_file)
	sujetos = OrderedDict(sorted(data['resultados'].items(), key=lambda t: t[0]))

	imprimirEncabezado()
	for sujeto in sujetos.values():
		procesarSujeto(sujeto)

def imprimirEncabezado():
	print("EsComputador", end=";")
	print("InmPcjAciertosTotal", end=";")
	print("InmPcjAciertosProf1", end=";")
	print("InmPcjAciertosProf2", end=";")
	print("InmPcjAciertosProf3", end=";")
	print("InmPcjAciertosLargo6", end=";")
	print("InmPcjAciertosLargo12", end=";")
	print("InmPcjAciertosLargo18", end=";")
	print("InmTPromTotal", end=";")
	print("InmTPromProf1", end=";")
	print("InmTPromProf2", end=";")
	print("InmTPromProf3", end=";")
	print("InmTPromLargo6", end=";")
	print("InmTPromLargo12", end=";")
	print("InmTPromLargo18", end=";")
	print("IncPcjAciertosTotal", end=";")
	print("IncPcjAciertosProf1", end=";")
	print("IncPcjAciertosProf2", end=";")
	print("IncPcjAciertosProf3", end=";")
	print("IncTPromTotal", end=";")
	print("IncTPromProf1", end=";")
	print("IncTPromProf2", end=";")
	print("IncTPromProf3", end=";")
	print()

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

def imprimirEsComputador(sujeto):
	if ('computacion' in sujeto['encuesta']['estudios']
		and sujeto['encuesta']['estudios']['computacion']):
		print(1, end=";")
	else:
		print(0, end=";")

def imprimirInmPcjAciertosTotal(sujeto):
	cantRespuestasCorrectas = 0
	cantRespuestas = 0
	for irt in sujeto['inmediato']['respuestas']:
		indice, respuesta, tiempo = irt[0], irt[1], irt[2]
		if secuencias_inmediato[indice]['respuesta'] == respuesta:
			cantRespuestasCorrectas += 1
		cantRespuestas += 1
	porcentaje = float(cantRespuestasCorrectas) / cantRespuestas
	print(round(porcentaje, 4), end=";")

def imprimirInmPcjAciertosPorProf(sujeto):
	cantRespuestasCorrectasPorProf = {p:0 for p in profundidades}
	cantRespuestasPorProf = {p:0 for p in profundidades}
	for irt in sujeto['inmediato']['respuestas']:
		indice, respuesta, tiempo = irt[0], irt[1], irt[2]
		if secuencias_inmediato[indice]['respuesta'] == respuesta:
			cantRespuestasCorrectasPorProf[secuencias_inmediato[indice]['prof']] += 1
		cantRespuestasPorProf[secuencias_inmediato[indice]['prof']] += 1
	for p in profundidades:
		porcentaje = float(cantRespuestasCorrectasPorProf[p]) / cantRespuestasPorProf[p]
		print(round(porcentaje, 4), end=";")

def imprimirInmPcjAciertosPorLargo(sujeto):
	cantRespuestasCorrectasPorLargo = {l:0 for l in largos}
	cantRespuestasPorLargo = {l:0 for l in largos}
	for irt in sujeto['inmediato']['respuestas']:
		indice, respuesta, tiempo = irt[0], irt[1], irt[2]
		if secuencias_inmediato[indice]['respuesta'] == respuesta:
			cantRespuestasCorrectasPorLargo[secuencias_inmediato[indice]['largo']] += 1
		cantRespuestasPorLargo[secuencias_inmediato[indice]['largo']] += 1
	for l in largos:
		porcentaje = float(cantRespuestasCorrectasPorLargo[l]) / cantRespuestasPorLargo[l]
		print(round(porcentaje, 4), end=";")

def imprimirInmTPromTotal(sujeto):
	tAcum = 0
	cantRespuestas = 0
	for irt in sujeto['inmediato']['respuestas']:
		indice, respuesta, tiempo = irt[0], irt[1], irt[2]
		if respuesta != 'X':
			tAcum += tiempo
			cantRespuestas += 1
	tProm = float(tAcum) / cantRespuestas
	print(round(tProm, 4), end=";")

def imprimirInmTPromPorProf(sujeto):
	tAcumPorProf = {p:0 for p in profundidades}
	cantRespuestasPorProf = {p:0 for p in profundidades}
	for irt in sujeto['inmediato']['respuestas']:
		indice, respuesta, tiempo = irt[0], irt[1], irt[2]
		if respuesta != 'X':
			tAcumPorProf[secuencias_inmediato[indice]['prof']] += tiempo
			cantRespuestasPorProf[secuencias_inmediato[indice]['prof']] += 1
	for p in profundidades:
		tProm = float(tAcumPorProf[p]) / cantRespuestasPorProf[p]
		print(round(tProm, 4), end=";")

def imprimirInmTPromPorLargo(sujeto):
	tAcumPorLargo = {l:0 for l in largos}
	cantRespuestasPorLargo = {l:0 for l in largos}
	for irt in sujeto['inmediato']['respuestas']:
		indice, respuesta, tiempo = irt[0], irt[1], irt[2]
		if respuesta != 'X':
			tAcumPorLargo[secuencias_inmediato[indice]['largo']] += tiempo
			cantRespuestasPorLargo[secuencias_inmediato[indice]['largo']] += 1
	for l in largos:
		tProm = float(tAcumPorLargo[l]) / cantRespuestasPorLargo[l]
		print(round(tProm, 4), end=";")

def imprimirIncPcjAciertosTotal(sujeto):
	cantRespuestasCorrectas = 0
	cantRespuestas = 0
	for irt in sujeto['inconsciente']['respuestas']:
		indice, respuesta, tiempo = irt[0], irt[1], irt[2]
		if secuencias_inconsciente[indice]['respuesta'] == respuesta:
			cantRespuestasCorrectas += 1
		cantRespuestas += 1
	porcentaje = float(cantRespuestasCorrectas) / cantRespuestas
	print(round(porcentaje, 4), end=";")

def imprimirIncPcjAciertosPorProf(sujeto):
	cantRespuestasCorrectasPorProf = {p:0 for p in profundidades}
	cantRespuestasPorProf = {p:0 for p in profundidades}
	for irt in sujeto['inconsciente']['respuestas']:
		indice, respuesta, tiempo = irt[0], irt[1], irt[2]
		if secuencias_inconsciente[indice]['respuesta'] == respuesta:
			cantRespuestasCorrectasPorProf[secuencias_inconsciente[indice]['prof']] += 1
		cantRespuestasPorProf[secuencias_inconsciente[indice]['prof']] += 1
	for p in profundidades:
		porcentaje = float(cantRespuestasCorrectasPorProf[p]) / cantRespuestasPorProf[p]
		print(round(porcentaje, 4), end=";")

def imprimirIncTPromTotal(sujeto):
	tAcum = 0
	cantRespuestas = 0
	for irt in sujeto['inconsciente']['respuestas']:
		indice, respuesta, tiempo = irt[0], irt[1], irt[2]
		if respuesta != 'X':
			tAcum += tiempo
			cantRespuestas += 1
	tProm = float(tAcum) / cantRespuestas
	print(round(tProm, 4), end=";")

def imprimirIncTPromPorProf(sujeto):
	tAcumPorProf = {p:0 for p in profundidades}
	cantRespuestasPorProf = {p:0 for p in profundidades}
	for irt in sujeto['inconsciente']['respuestas']:
		indice, respuesta, tiempo = irt[0], irt[1], irt[2]
		if respuesta != 'X':
			tAcumPorProf[secuencias_inconsciente[indice]['prof']] += tiempo
			cantRespuestasPorProf[secuencias_inconsciente[indice]['prof']] += 1
	for p in profundidades:
		tProm = float(tAcumPorProf[p]) / cantRespuestasPorProf[p]
		print(round(tProm, 4), end=";")

if __name__ == '__main__':
	main()