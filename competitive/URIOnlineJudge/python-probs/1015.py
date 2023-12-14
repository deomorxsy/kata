#!usr/bin/env python3

'''
Iniciante
Problema 1015 do URI Online Judge
https://www.urionlinejudge.com.br/judge/pt/problems/view/1015

Distância Entre Dois Pontos
'''

def main():
	'''
	Lê quatro valores correspondentes aos eixos x e y de dois pontos
	quaisquer no plano, p1(x1,y1), p2(x2,y2) e calcula a distância entre eles,
	mostrando 4 casas decimais após a vírgula
	'''
	x1, y1 = [float(i) for i in input().split()]         #p1

	x2, y2 = [float(i) for i in input().split()]         #p2

	distância = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

	print('{:.4f}' .format(distância))



if __name__ == '__main__':
	main()