#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from collections import OrderedDict
from pprint import pprint

profundidades = [1, 2, 3]
largos = [6, 12, 18]
t_expo_inmediato =  {6:300, 12: 520, 18:  1000}
t_inconsciente = 1000

t_prev_letras = 1000      # tiempo de espera antes de la tarea secundaria
t_expo_letras = 600       # cada letra se muestra 500ms
t_resp_letras = 15000       # la respuesta se da en 2000ms
t_buff_letras = 1000       # intervalo despues de responder la ultima letra
t_primeras_letras = 1000
t_buff = 150
t_expo = 1000

def restarTInc(rtasLetras, indice, tiempo):
	t_rta_letras = 0
	for i in range(0,3):
		rta_letra = rtasLetras[indice*3+i][3]
		# Hago chequeo para ver si no me sumo "-1" en vez de 15000. 
		# solo acá hay que hacerlo, porque si me poné el -1 pero en el total tiene en cuenta el 15000 es rompe tooo
		if rta_letra < 0:
			rta_letra = 15000
		t_rta_letras+=rta_letra
	t_rta_letras-=3*t_expo_letras

	# print("tiempo: ", tiempo, "t_expo: ", t_expo, "t_prev_letras: ", t_prev_letras, "t_expo_letras: ", 5*t_expo_letras)
	# print("t_primeras_letras:", 2*t_primeras_letras, "t_rta_letras: ", t_rta_letras, "t_buff: ", 3*t_buff, "t_buff_letras: ", t_buff_letras)

	# Esta es la corrección del tiempo:
	# se le resta el tiempo de expo de la secuencia, el tiempo prev a mostrar las letras, el tiempo de expo de las letras
	# que son 5, el t de las 2 primeras letras, se resta la suma del tiempo de rta en las letras del invididuo (al cual se le resto ya
	# 	el tiempo de exposición de las letras), se resta el t_buff que solo esta para 3 letras, y por ultimo el t_buff del final 
	# de la expoosición de letras
	return tiempo - t_expo - t_prev_letras - 5*(t_expo_letras) - 2*t_primeras_letras - t_rta_letras - 3*t_buff - t_buff_letras


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
	print("EsComputador", end=",")
	print("InmPcjAciertosTotal", end=",")
	print("InmPcjAciertosProf1", end=",")
	print("InmPcjAciertosProf2", end=",")
	print("InmPcjAciertosProf3", end=",")
	print("InmPcjAciertosLargo6", end=",")
	print("InmPcjAciertosLargo12", end=",")
	print("InmPcjAciertosLargo18", end=",")
	print("InmTPromTotal", end=",")
	print("InmTPromProf1", end=",")
	print("InmTPromProf2", end=",")
	print("InmTPromProf3", end=",")
	print("InmTPromLargo6", end=",")
	print("InmTPromLargo12", end=",")
	print("InmTPromLargo18", end=",")
	print("IncPcjAciertosTotal", end=",")
	print("IncPcjAciertosProf1", end=",")
	print("IncPcjAciertosProf2", end=",")
	print("IncPcjAciertosProf3", end=",")
	print("IncTPromTotal", end=",")
	print("IncTPromProf1", end=",")
	print("IncTPromProf2", end=",")
	print("IncTPromProf3", end=",")
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
		print(1, end=",")
	else:
		print(0, end=",")

def imprimirInmPcjAciertosTotal(sujeto):
	cantRespuestasCorrectas = 0
	cantRespuestas = 0
	for irt in sujeto['inmediato']['respuestas']:
		indice, respuesta, tiempo = irt[0], irt[1], irt[2]
		if secuencias_inmediato[indice]['respuesta'] == respuesta:
			cantRespuestasCorrectas += 1
		cantRespuestas += 1
	porcentaje = float(cantRespuestasCorrectas) / cantRespuestas
	print(round(porcentaje, 4), end=",")

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
		print(round(porcentaje, 4), end=",")

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
		print(round(porcentaje, 4), end=",")

def imprimirInmTPromTotal(sujeto):
	tAcum = 0
	cantRespuestas = 0
	for irt in sujeto['inmediato']['respuestas']:
		indice, respuesta, tiempo = irt[0], irt[1], irt[2]
		# resto el tiempo exposición que por error lo incluimos
		tiempo -= t_expo_inmediato[secuencias_inmediato[indice]['largo']]
		if respuesta != 'X':
			tAcum += tiempo
			cantRespuestas += 1
	tProm = float(tAcum) / cantRespuestas
	print(round(tProm, 4), end=",")

def imprimirInmTPromPorProf(sujeto):
	tAcumPorProf = {p:0 for p in profundidades}
	cantRespuestasPorProf = {p:0 for p in profundidades}
	for irt in sujeto['inmediato']['respuestas']:
		indice, respuesta, tiempo = irt[0], irt[1], irt[2]
		# resto el tiempo exposición que por error lo incluimos
		tiempo -= t_expo_inmediato[secuencias_inmediato[indice]['largo']]
		if respuesta != 'X':
			tAcumPorProf[secuencias_inmediato[indice]['prof']] += tiempo
			cantRespuestasPorProf[secuencias_inmediato[indice]['prof']] += 1
	for p in profundidades:
		tProm = float(tAcumPorProf[p]) / cantRespuestasPorProf[p]
		print(round(tProm, 4), end=",")

def imprimirInmTPromPorLargo(sujeto):
	tAcumPorLargo = {l:0 for l in largos}
	cantRespuestasPorLargo = {l:0 for l in largos}
	for irt in sujeto['inmediato']['respuestas']:
		indice, respuesta, tiempo = irt[0], irt[1], irt[2]
		# resto el tiempo exposición que por error lo incluimos
		tiempo -= t_expo_inmediato[secuencias_inmediato[indice]['largo']]
		if respuesta != 'X':
			tAcumPorLargo[secuencias_inmediato[indice]['largo']] += tiempo
			cantRespuestasPorLargo[secuencias_inmediato[indice]['largo']] += 1
	for l in largos:
		tProm = float(tAcumPorLargo[l]) / cantRespuestasPorLargo[l]
		print(round(tProm, 4), end=",")

def imprimirIncPcjAciertosTotal(sujeto):
	cantRespuestasCorrectas = 0
	cantRespuestas = 0
	for irt in sujeto['inconsciente']['respuestas']:
		indice, respuesta, tiempo = irt[0], irt[1], irt[2]
		if secuencias_inconsciente[indice]['respuesta'] == respuesta:
			cantRespuestasCorrectas += 1
		cantRespuestas += 1
	porcentaje = float(cantRespuestasCorrectas) / cantRespuestas
	print(round(porcentaje, 4), end=",")

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
		print(round(porcentaje, 4), end=",")

def imprimirIncTPromTotal(sujeto):
	tAcum = 0
	cantRespuestas = 0
	for irt in sujeto['inconsciente']['respuestas']:
		indice, respuesta, tiempo = irt[0], irt[1], irt[2]
		# Tiempo corregido para inconsciente:
		tiempo = restarTInc(sujeto['inconsciente']['respuestasLetras'], indice, tiempo)
		if respuesta != 'X':
			tAcum += tiempo
			cantRespuestas += 1
	tProm = float(tAcum) / cantRespuestas
	print(round(tProm, 4), end=",")

def imprimirIncTPromPorProf(sujeto):
	tAcumPorProf = {p:0 for p in profundidades}
	cantRespuestasPorProf = {p:0 for p in profundidades}
	for irt in sujeto['inconsciente']['respuestas']:
		indice, respuesta, tiempo = irt[0], irt[1], irt[2]
		# Tiempo corregido para inconsciente:
		tiempo = restarTInc(sujeto['inconsciente']['respuestasLetras'], indice, tiempo)
		if respuesta != 'X':
			tAcumPorProf[secuencias_inconsciente[indice]['prof']] += tiempo
			cantRespuestasPorProf[secuencias_inconsciente[indice]['prof']] += 1
	for p in profundidades:
		tProm = float(tAcumPorProf[p]) / cantRespuestasPorProf[p]
		print(round(tProm, 4), end=",")

if __name__ == '__main__':
	main()