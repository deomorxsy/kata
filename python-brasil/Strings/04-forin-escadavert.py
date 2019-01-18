#! usr/bin/env/python3

'''
Autor: deomorxsy
Data: 18/01/2019

Exercícios com Strings nº 04 do Python Wiki BR
https://wiki.python.org.br/ExerciciosComStrings

Nome na vertical em escada.
/// Estrutura de Repetição FOR IN

Slicing em Python -> start:stop:steps
'''

def main():
	name = input()
	index = 1
	y = len(name) - 1

	# Para ITEM em NAME, imprima name[:index]. Ou seja, comece em 0 e pare em 1.
	#Mostrará a primeira letra.
	for i in name:
		print(name[:index])
		index += 1 #Essa linha altera o valor de index para que a escada aconteça. 

if __name__ == '__main__':
	main()