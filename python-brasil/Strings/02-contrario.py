#! usr/bin/env/python3

'''
Autor: deomorxsy
Data: 18/01/2019

Exercícios com Strings nº 02 do Python Wiki BR
https://wiki.python.org.br/ExerciciosComStrings

Nome ao contrário em maiúsculas.
'''

def main():
	#Lê um nome String e imprime o seu contrário em letra maiúscula (caixa alta)
	name = input()

	#Utilizando método Slicing para inverter a ordem da lista
	y = name[::-1]
	print('{}' .format(y.upper()))


if __name__ == '__main__':
	main()