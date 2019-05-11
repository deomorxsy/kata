#!usr/bin/env/python3
'''
03ª Questão, página 03 - IF-Camboriú Caderno de Algoritmos
'''

def main():
	'''
	Questão 03 - Letra A
	'''
	one = {
		'A' : 3,
		'B' : 16,
		'nome' : 'miriam',
		'prof' : 'advogado',
	}

	two = {
		'A' : 5,
		'B' : 64,
		'nome' : 'pedro', 
		'prof' : 'medico',
	}

	three = {
		'A' : 2.5,
		'B' : 9,
		'nome' : 'ana', 
		'prof' : 'professor',
	}

	if one['A'] + 1 >= (int(one['B'] ** 1/2)) or one['nome'] != 'ana':
		return True
	else:
		return False


print(main())


if '__name__' == '__main__':
	main()