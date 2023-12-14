#Exercício 1
#Escreva um programa que receba um número natural n na entrada
# e imprima n! (fatorial) na saída.
num = 1
n = int(input("Digite o valor de n: "))

while n >= 1:
    num *= n
    n -= 1	#Update n
print(num)