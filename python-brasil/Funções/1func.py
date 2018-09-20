#1func 
	#Faça um programa para imprimir para um n informado pelo usuário.
	#Use uma função que receba um valor n inteiro e imprima
	#até a n-ésima linha. 

n = int(input('Digite um n: '))

def func(n):
	num = n
	n -= n
	while num >=1:
		n += 1
		print(n)
		num -= 1
	return n

func(n)















#https://wiki.python.org.br/ExerciciosFuncoes