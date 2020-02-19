#!usr/bin/env/python3
# 7kyu Kata. Binary Addition
# Check at https://www.codewars.com/kata/binary-addition

'''
Implement a function that adds two numbers together and returns their sum in binary.
The conversion can be done before, or after the addition. The binary number returned should be a string.
'''
def add_binary(a,b):
	#your code here
	c = a + b # 63.
	acc_dvden = [c] # DIVIDENDO: Accumulator Variable that will hold the DIVIDEND iteration reassignments. acc_dvden[0] é 63, c.
	acc_resto = [] # RESTO: Accumulator Variable that will hold the REMAINDER iteration reassignments.
	index = 0 #Item Index. It fits for both 

	while acc_dvden[index] >= 1:
		acc_dvden.append(acc_dvden[index] // 2) # Divisão Inteira
		acc_resto.append(str(acc_dvden[index] % 2)) # Adquirindo o Resto
		
		index += 1 # Para que o index atualize e siga o laço de repetição.

	return ''.join(acc_resto[::-1]) # Método de String join(), seguido do Fatiamento(slicing) de Lista que a retorna ao contrário.

'''
Solution:

Using the math algorithm of conversion from Decimal to Binary, we can do it without rely in any other built-in function such as bin().
In fact, this is useful even in other languages.

Algoritmo: Conversão de decimal para binário e vice-versa
# link: https://educacao.uol.com.br/disciplinas/matematica/numeros-binarios-2-conversao-para-decimais.htm
'''