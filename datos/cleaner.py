#!/usr/bin/env python3

import json
from collections import OrderedDict
from pprint import pprint

secuencias_inmediato = [
	{'largo': 18, 'rta_correcta': 'N', 'depth':2},
	{'largo': 18, 'rta_correcta': 'N', 'depth':2},
	{'largo': 18, 'rta_correcta': 'N', 'depth':1},
	{'largo': 12, 'rta_correcta': 'N', 'depth':3},
	{'largo': 18, 'rta_correcta': 'S', 'depth':2},
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
	cant_rtas_correctas_inmediato = 0
	for rta_tiempo in sujeto['inmediato']['respuestas']:
		indice, rta, tiempo  = rta_tiempo[0], rta_tiempo[1], rta_tiempo[2]
		if secuencias_inmediato[indice]['rta_correcta'] == rta:
			cant_rtas_correctas_inmediato = cant_rtas_correctas_inmediato + 1
	print(cant_rtas_correctas_inmediato)

def main():
	data = None
	with open('incc-tp1-export-16oct.json') as data_file:
		data = json.load(data_file)
	sujetos = OrderedDict(sorted(data['resultados'].items(), key=lambda t: t[0]))
	for key in sujetos:
		sujeto = sujetos[key]
		procesarSujeto(sujeto)

if __name__ == '__main__':
	main()