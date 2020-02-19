#! usr/bin/env/python3

'''
Iniciante
Problema 1018 do URI Online Judge
https://www.urionlinejudge.com.br/judge/pt/problems/view/1018

Cédulas
'''

def main():
	'''
	#Lê o número de entrada e imprime a quantidade mínima de cédulas para o valor
	'''
	valor = int(input())

	print(valor)

	print('{} nota(s) de R$ 100,00' .format(valor // 100))
	valor %= 100

	print('{} nota(s) de R$ 50,00' .format(valor // 50))
	valor %= 50

	print('{} nota(s) de R$ 20,00' .format(valor // 20))
	valor %= 20

	print('{} nota(s) de R$ 10,00' .format(valor // 10))
	valor %= 10

	print('{} nota(s) de R$ 5,00' .format (valor // 5))
	valor %= 5

	print('{} nota(s) de R$ 2,00' .format(valor // 2))
	valor %= 2

	print('{} nota(s) de R$ 1,00' .format(valor // 1))





if __name__ == '__main__':
	main()