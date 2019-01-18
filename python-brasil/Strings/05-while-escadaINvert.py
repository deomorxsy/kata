#! usr/bin/env/python3

'''
Autor: deomorxsy
Data: 18/01/2019

Exercícios com Strings nº 05 do Python Wiki BR
https://wiki.python.org.br/ExerciciosComStrings

Nome na vertical em escada invertida.
/// Estrutura de Repetição WHILE

Slicing em Python -> start:stop:steps
'''

def main():
	name = input()
	index = -1
	y = len(name) - 1
	var = 1

	#Enquanto neg for menor ou igual a quantidade de itens em NAME,
	#imprima NAME em escada de trás para frente
	while var < len(name) + 1:
		print(name[:index])
		index -= 1
		var += 1

if __name__ == '__main__':
	main()