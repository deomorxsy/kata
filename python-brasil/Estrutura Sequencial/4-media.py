#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1 = int(input('Digite a primeira média: '))
n2 = int(input('Digite a segunda média: '))
n3 = int(input('Digite a terceira média: '))
n4 = int(input('Digite a quarta média: '))

medint = (n1 + n2 + n3 + n4) // 4
med = (n1 + n2 + n3 + n4) / 4

print ('A Média Inteira é: ', medint)
print('A Média Normal é: ', med)
