print("=================")
print("soma dos dígitos")
print("=================")

n = int(input("Digite um número: "))

aux = n
soma = 0
#aux = Variável auxiliar.
#soma = Variável de armazenagem a cada iteração
while (aux > 0):
	soma += (aux % 10)
	aux = (aux//10)
	if (aux == 0):
		print (soma)
