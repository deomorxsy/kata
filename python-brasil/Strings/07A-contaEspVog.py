#! usr/bin/env/python3

def main():
	#Quantidade de espaços em branco
	x = input()
	y = x.split() #O split transformará os itens separados por espaços em índices de Lista.

	print('Existem {} espaços em branco na frase.' .format(len(y) - 1)) 
	#Acima, a quantidade de espaços é a quantidade de índices de lista - 1.

if __name__ == '__main__':
	main()

'''
Autor: deomorxsy
Data: 21/01/2019

PARTE 1
/// Exercícios com Strings nº 07 do Python Wiki BR
https://wiki.python.org.br/ExerciciosComStrings
'''