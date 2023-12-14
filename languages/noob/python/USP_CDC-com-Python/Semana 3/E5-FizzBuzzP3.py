n1 = int(input("Digite um número inteiro: "))
n2 = (n1 % 3)
n3 = (n1 % 5)
if ((n2 == 0) and (n3 == 0)):
	print("FizzBuzz")
else:
	print(n1)
	