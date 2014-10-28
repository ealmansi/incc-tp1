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
	respuestas = filtrarRespuestasInm(sujeto, {})
	respuestasCorrectas = filtrarRespuestasInm(sujeto, {'soloCorrectas': True})
	porcentaje = float(len(respuestasCorrectas)) / len(respuestas)
	print("%.4f" % porcentaje, end=",")

def imprimirInmPcjAciertosPorProf(sujeto):
	for p in profundidades:
		respuestas = filtrarRespuestasInm(sujeto, {'prof': p})
		respuestasCorrectas = filtrarRespuestasInm(sujeto, {'prof': p, 'soloCorrectas': True})
		porcentaje = float(len(respuestasCorrectas)) / len(respuestas)
		print("%.4f" % porcentaje, end=",")

def imprimirInmPcjAciertosPorLargo(sujeto):
	for l in largos:
		respuestas = filtrarRespuestasInm(sujeto, {'largo': l})
		respuestasCorrectas = filtrarRespuestasInm(sujeto, {'largo': l, 'soloCorrectas': True})
		porcentaje = float(len(respuestasCorrectas)) / len(respuestas)
		print("%.4f" % porcentaje, end=",")

def imprimirInmTPromTotal(sujeto):
	respuestasCorrectas = filtrarRespuestasInm(sujeto, {'soloCorrectas': True})
	tAcum = 0
	for irt in respuestasCorrectas:
		tAcum += tiempoCorregidoInm(irt)
	tProm = float(tAcum) / len(respuestasCorrectas)
	print("%.4f" % tProm, end=",")

def imprimirInmTPromPorProf(sujeto):
	for p in profundidades:
		respuestasCorrectas = filtrarRespuestasInm(sujeto, {'prof': p, 'soloCorrectas': True})
		tAcum = 0
		for irt in respuestasCorrectas:
			tAcum += tiempoCorregidoInm(irt)
		tProm = float(tAcum) / len(respuestasCorrectas)
		print("%.4f" % tProm, end=",")

def imprimirInmTPromPorLargo(sujeto):
	for l in largos:
		respuestasCorrectas = filtrarRespuestasInm(sujeto, {'largo': l, 'soloCorrectas': True})
		tAcum = 0
		for irt in respuestasCorrectas:
			tAcum += tiempoCorregidoInm(irt)
		tProm = float(tAcum) / len(respuestasCorrectas)
		print("%.4f" % tProm, end=",")

def imprimirIncPcjAciertosTotal(sujeto):
	respuestas = filtrarRespuestasInc(sujeto, {})
	respuestasCorrectas = filtrarRespuestasInc(sujeto, {'soloCorrectas': True})
	porcentaje = float(len(respuestasCorrectas)) / len(respuestas)
	print("%.4f" % porcentaje, end=",")

def imprimirIncPcjAciertosPorProf(sujeto):
	for p in profundidades:
		respuestas = filtrarRespuestasInc(sujeto, {'prof': p})
		respuestasCorrectas = filtrarRespuestasInc(sujeto, {'prof': p, 'soloCorrectas': True})
		porcentaje = float(len(respuestasCorrectas)) / len(respuestas)
		print("%.4f" % porcentaje, end=",")

def imprimirIncTPromTotal(sujeto):
	respuestasCorrectas = filtrarRespuestasInc(sujeto, {'soloCorrectas': True})
	cantRespuestasContadas = 0
	tAcum = 0
	for irt in respuestasCorrectas:
		tiempo = tiempoCorregidoInc(irt, sujeto['inconsciente']['respuestasLetras'])
		if tiempo > 100:
			tAcum += tiempo
			cantRespuestasContadas += 1
	tProm = float(tAcum) / cantRespuestasContadas
	print("%.4f" % tProm, end=",")

def imprimirIncTPromPorProf(sujeto):
	for p in profundidades:
		respuestasCorrectas = filtrarRespuestasInc(sujeto, {'prof': p, 'soloCorrectas': True})
		cantRespuestasContadas = 0
		tAcum = 0
		for irt in respuestasCorrectas:
			tiempo = tiempoCorregidoInc(irt, sujeto['inconsciente']['respuestasLetras'])
			if tiempo > 100:
				tAcum += tiempo
				cantRespuestasContadas += 1
		tProm = float(tAcum) / cantRespuestasContadas
		print("%.4f" % tProm, end=",")

# # # # # # # # # # # # # # # # # # # #

def filtrarRespuestasInm(sujeto, criterio):
	respuestas = []
	for irt in sujeto['inmediato']['respuestas']:
		indice, respuesta, tiempo = irt[0], irt[1], irt[2]
		if ('prof' in criterio
				and secuencias_inmediato[indice]['prof'] != criterio['prof']):
			continue
		if ('largo' in criterio
				and secuencias_inmediato[indice]['largo'] != criterio['largo']):
			continue
		if ('soloCorrectas' in criterio and criterio['soloCorrectas'] == True
			and secuencias_inmediato[indice]['respuesta'] != respuesta):
			continue
		respuestas.append(irt)
	return respuestas

def filtrarRespuestasInc(sujeto, criterio):
	respuestas = []
	for irt in sujeto['inconsciente']['respuestas']:
		indice, respuesta, tiempo = irt[0], irt[1], irt[2]
		if ('prof' in criterio
				and secuencias_inconsciente[indice]['prof'] != criterio['prof']):
			continue
		if ('soloCorrectas' in criterio and criterio['soloCorrectas'] == True
			and secuencias_inconsciente[indice]['respuesta'] != respuesta):
			continue
		respuestas.append(irt)
	return respuestas

# # # # # # # # # # # # # # # # # # # #

def tiempoCorregidoInm(irt):
	indice, _, tiempo = irt[0], irt[1], irt[2]
	return tiempo - t_expo_inmediato[secuencias_inmediato[indice]['largo']]

# # # # # # # # # # # # # # # # # # # #
# Esta es la corrección del tiempo para el inconsciente:
# se le resta el tiempo de expo de la secuencia, el tiempo prev a mostrar las letras, el tiempo de expo de las letras
# que son 5, el t de las 2 primeras letras, se resta la suma del tiempo de rta en las letras del invididuo (al cual se le resto ya
# 	el tiempo de exposición de las letras), se resta el t_buff que solo esta para 3 letras, y por ultimo el t_buff del final 
# de la expoosición de letras
# # # # # # # # # # # # # # # # # # # #
def tiempoCorregidoInc(irt, rtasLetras):
	indice, _, tiempo = irt[0], irt[1], irt[2]
	t_rta_letras = 0
	for i in range(0, 3):
		rta_letra = rtasLetras[indice * 3 + i][3]
		# Hago chequeo para ver si no me sumo "-1" en vez de 15000. 
		# solo acá hay que hacerlo, porque si me poné el -1 pero en el total tiene en cuenta el 15000 es rompe tooo
		if rta_letra < 0:
			rta_letra = 15000
		t_rta_letras += rta_letra
	t_rta_letras -= 3 * t_expo_letras
	return (tiempo - t_expo - t_prev_letras
		- 5 * (t_expo_letras) - 2 * t_primeras_letras
		- t_rta_letras - 3 * t_buff - t_buff_letras)

if __name__ == '__main__':
	main()