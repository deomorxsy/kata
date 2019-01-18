#! usr/bin/env/python3

'''
Autor: deomorxsy
Data: 18/01/2019

Exercícios com Strings nº 03 do Python Wiki BR
https://wiki.python.org.br/ExerciciosComStrings

Nome na vertical.
'''

def main():
	#Faça um programa que solicite o nome do usuário e imprima-o na vertical. 
	name = input()
	index = 0

	# Para ITEM em NAME, imprima index 0 até a quantidade máxima de ITENS em NAME
	for i in name:
		print(name[index])
		index += 1 #Essa linha altera o valor de index. Último item do LOOP for in 

if __name__ == '__main__':
	main()
