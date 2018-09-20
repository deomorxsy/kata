#Exercício 3
#Escreva um programa que receba um número inteiro na entrada,
#calcule e imprima a soma dos dígitos deste número na saída.

n = int(input("Digite um número inteiro: "))
var = 0 #variável de somatório dos dígitos

while n > 0:
	var += n % 10
	n //= 10 #update
print(var)