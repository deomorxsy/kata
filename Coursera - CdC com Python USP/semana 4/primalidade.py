#Exercício Adicional 1

#Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

n = int(input("Digite um n: "))
p = n // 2

while n > 0:
	if (n != 1) and (p % 2) != 0:
		print("primo")
		n -= n #FLAG. Indicador de passagem
	else: #if (n = 1) and (p % 2) == 0:
		print("não é primo")
		n -= n #FLAG. Indicador de passagem