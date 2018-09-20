#fatfun test.py

def fatfun(n): #anteriormente com n, num
	num = 1 #definindo a variável, dentro da função
	while n >= 1:
		num *= n
		n -= 1 #update n
	print(num)