import math
print("=================================================================")
print("Fórmula de Bháskara - Um programa para encontrar Raízes da Função")
print("=================================================================")

a  = float(input("Insira o valor do Coeficiente a: "))
b  = float(input("Insira o valor do Coeficiente b: "))
c  = float(input("Insira o valor do Coeficiente c: "))

a != 0
delta = (b**2 - 4 * a * c)
if (delta < 0):
	print("O valor do delta é ", delta,"e esta equação não possui raízes reais")
elif ((delta > 0) or (delta == 0)):
	math.sqrt(delta)
	raiz1 = (-b + delta / 2 * a)
	raiz2 = (-b - delta / 2 * a)
	if (delta > 0):
		print("O valor do Delta é", delta, "e tem duas Raízes.")
		print("A primeira raiz é: ", raiz1)
		print("A segunda raiz é: ", raiz2)
	elif (delta == 0):
		print("O valor do Delta é", delta, "e tem uma Raíz.")
		print("O valor da raiz é: ", raiz1)
	
	
	

