#!usr/bin/env python3

'''
Iniciante
Problema 1014 do URI Online Judge
https://www.urionlinejudge.com.br/judge/pt/problems/view/1014

Consumo
'''

def main():
	'''
	Cálculo do consumo médio de um automóvel sendo fornecidos a distância total
	percorrida (em Km) e o total de combustível gasto (em litros).
	'''
	x, y = int(input()), float(input())

	consumo_med = float(x / y )

	print('{:.3f} km/l' .format(consumo_med))





if __name__ == '__main__':
	main()