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
	print("esta equação não possui raízes reais")
elif ((delta > 0) or (delta == 0)):
	math.sqrt(delta)
	x = (-b - delta / 2 * a)
	y = (-b + delta / 2 * a)
	if (delta > 0):
		print("as raízes da equação são", x, "e", y, ".")
	elif (delta == 0):
		print("a raiz desta equação é", x)
	
	
	

