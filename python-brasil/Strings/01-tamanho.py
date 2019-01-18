#! usr/bin/env/python3
#Autor: deomorxsy
#Data: 25/12/2018

def main():
	#Lê 2 strings, informa o conteúdo seguido do comprimento de ambas.
	s1, s2 = input(), input()

	print('String 1: {} \nString 2: {}' .format(s1,s2))
	print('Tamanho de "{}": {}' .format(s1,len(s1)))
	print('Tamanho de "{}": {}' .format(s2,len(s2)))
	#Comparando Tamanho
	if len(s1) == len(s2):
		print('As duas strings são de tamanhos iguais.')

		#Comparando Conteúdo
		if s1 == s2:
			print('As duas strings possuem mesmo conteúdo.' )
		else:
			print('As duas strings possuem conteúdo diferente.')

	else:
		print('As duas strings são de tamanhos diferentes.')

	#Comparando conteúdo

if __name__ == '__main__':
	main()