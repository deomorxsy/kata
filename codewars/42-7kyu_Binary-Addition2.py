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

	return ''.join(acc_resto[::-1])

	return ''.join(acc_resto[::-1]) while acc_dvden[index] >= 1