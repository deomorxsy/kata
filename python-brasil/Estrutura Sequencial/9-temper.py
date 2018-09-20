#Faça um Programa que peça a temperatura em graus Farenheit, transforme
# e mostre a temperatura em graus Celsius.
#	C = (5 * (F-32) / 9). 

f = int(input('Digite os graus em Fahrenheit: '))

fc = (5 * (f-32) / 9) #real
FC = (5 * (f-32) // 9) #inteiro

print('Em Celsius, essa Temperatura é de:', fc, FC)

cf = ((f - 32) / 1.8)
CF = ((f - 32) // 1.8)