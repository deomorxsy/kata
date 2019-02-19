#! usr/bin/env/python3

def bonus_time(salary, bonus):
	newsal = 0   # Variável de iteração; guardará o salário se houver bônus.

	if float(bonus) == True:
		#Como pedido pelo problema, na linha 9 adapto 'salary' para ser um Integral.
		#Na linha 10  e 12 o uso de format é desnecessário, porém bom para organização.
		newsal = (int(salary) * 10) 
		return ('${}' .format(newsal))
	else:
		return ('${}' .format(salary))

if '__name__' == '__main__':
	main()


'''
#Autor: deomorxsy
#Data: 18/02/2019

/// Do I get a bonus? - A.Partridge

https://www.codewars.com/kata/do-i-get-a-bonus/train/python
'''