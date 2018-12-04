#! usr/bin/env/python3

'''
Iniciante
Problema 1019 do URI Online Judge
https://www.urionlinejudge.com.br/judge/pt/problems/view/1019

Conversão de tempo
'''

def main():
	#Converte um valor INT de segundos em formato HORAS, MINUTOS E SEGUNDOS.
	t = int(input())

	hour = t // 3600
	t %= 3600 

	# Iteração necessária para que o próximo valor tenha como base o valor
	# anterior, que nesse caso é a hora.


	minute = t // 60
	t %= 60
	# Iteração necessária para que o próximo valor tenha como base o valor
	# anterior, que nesse caso é o minuto.
	second = t


	print('{}:{}:{}' .format(hour, minute, second))



if __name__ == '__main__':
	main()