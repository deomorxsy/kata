#! usr/bin/env/python3

'''
Iniciante
Problema 1017 do URI Online Judge
https://www.urionlinejudge.com.br/judge/pt/problems/view/1017

Gasto de Combustível
'''

def main():
	'''
	1L faz 12KM

	Tempo gasto na viagem em Horas, Velocidade Média em Km/h
	'''
	tempo,vm  = int(input()), int(input())

	consumo = float(tempo * vm / 12)

	print('{:.3f}' .format(consumo))
	


if __name__ == '__main__':
	main()