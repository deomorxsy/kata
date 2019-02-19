#! usr/bin/env/python3

def no_space(x):
	y = x.split() # Leia as notas na linha 10
	delimiter = '' # Definimos um delimitador vazio, sem espaços. Servirá como argumento join
	z = delimiter.join(y) # Notas na linha 15

	return delimiter.join(y)

    # Na linha 4, o método .split() é usado para quebrar Strings em palavras.
    # O argumento padrão dentro dos parênteses é vazio, ou seja, todos os espaços em branco;
    # caso necessário especificar um limite, então você pode especificar um 
    # 'delimiter' (linha 5) entre os parênteses, como vírgulas, travessões, e traços.

    # A linha 6 acima juntará todos os itens da lista 'y'
	# com base no delimitador 'delimiter' e atribuirá à variável 'z'


if '__name__' == '__main__':
	main()

'''
#Autor: deomorxsy
#Data: 16/02/2019

/// Remove String Spaces - A.Partridge

https://www.codewars.com/kata/remove-string-spaces/train/python
'''