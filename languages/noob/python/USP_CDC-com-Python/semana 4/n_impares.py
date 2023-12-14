#Exercício 2
#Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

#número de vezes que irá escrever os números/números
n = int(input("Digite o valor de n: "))
var = n - 1
num = 1

while var >= 0:
	print(num)
	var -= 1	#update n
	num += 2 #update num