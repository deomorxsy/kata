#! usr/bin/env/python3

#EM CONSTRUÇÃO

def main():
	#CONTADOR - Quantidade de vogais
	x = input()
	count = 0
	
	for letter in x:
		if letter == 'a' and 'i' and 'u' and 'e' and 'o':
			count += 1 #Aqui vemos um exemplo de VARIÁVEL DE CONTROLE CONTADOR,
			           #diferente de VARIÁVEL DE CONTROLE. LOOP
	print(count)

if __name__ == '__main__':
	main()


'''
Autor: deomorxsy
Data: 21/01/2019

PARTE 3
/// Exercícios com Strings nº 07 do Python Wiki BR
https://wiki.python.org.br/ExerciciosComStrings
'''