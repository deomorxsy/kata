#! usr/bin/env/python3

'''
Autor: deomorxsy
Data: 18/01/2019

Exercícios com Strings nº 04 do Python Wiki BR
https://wiki.python.org.br/ExerciciosComStrings

Nome na vertical em escada
/// Estrutura de Repetição WHILE

Slicing em Python -> start:stop:steps
'''

def main():
	name = input()
	index = 1
	y = len(name) - 1

	#Enquanto INDEX for menor ou igual a quantidade de índices em NAME,
	#imprima NAME em escada
	while index <= len(name):
		print(name[:index])
		index += 1

if __name__ == '__main__':
	main()