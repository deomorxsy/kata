#! usr/bin/env/python3

'''
Autor: deomorxsy
Data: 18/01/2019

Exercícios com Strings nº 06 do Python Wiki BR
https://wiki.python.org.br/ExerciciosComStrings

Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa)
do usuário e imprima a data com o nome do mês por extenso. 

/// Utilizo o método Split duas vezes para que possa transformar os itens
    separados por vírgula da String em uma Lista com vários índices.
'''

def main():
	date = input('Data de Nascimento: ')
	datesplit = date.split('/') #Utilizei o método .split para transformar os itens separados por / em itens de Lista
	
	day, month, year = datesplit[0], int(datesplit[1]), datesplit[2] 
	# Transformo o item 1 da lista em INTEIRO para poder utilizá-lo na Lista de Meses abaixo

	x = 'Janeiro, Fevereiro, Março, Abril, Maio, Junho, Julho, Agosto, Setembro, Outubro, Novembro, Dezembro'
	meses = x.split(',')
	#Acima transformei a variável x (que era do tipo String) em Lista com o método .split()

	print('Você nasceu em {} de{} de {}.' .format(day, meses[month - 1], year))
	'''///Aqui faço uso do método .format() para substituir as variáveis
	em suas devidas chaves, para organizar melhor as informações'''

if __name__ == '__main__':
	main()
