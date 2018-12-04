#! usr/bin/env/python3

'''
Iniciante
Problema 1020 do URI Online Judge
https://www.urionlinejudge.com.br/judge/pt/problems/view/1020

Idade em Dias
aid = Age in Days
'''

def main():
	aid = int(input())

	years = aid // 365
	aid %= 365

	# Esse bloco realiza divisão INTEIRA e itera(atualiza) AID com o
	# RESTO DA DIVISÃO (módulo, que é o excedente) por 365 dias

	months = aid // 30
	aid %= 30

	# Esse bloco realiza divisão INTEIRA para o MÊS e itera(atualiza) AID com o
	# RESTO DA DIVISÃO (módulo, que é o excedente) por 30 dias

	days = aid

	# Esse bloco pega o RESTO DA DIVISÃO (módulo, que é o excedente) dos 30 dias
	# Desse modo, se no bloco anterior tiver sobrado algum dia a mais, esse mostrará

	print('{} ano(s)' .format(years))
	print('{} mes(es)' .format(months))
	print('{} dia(s)' .format(days))



if __name__ == '__main__':
	main()