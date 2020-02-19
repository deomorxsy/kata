#!usr/bin/env python3

'''
Iniciante
Problema 1012 do URI Online Judge
https://www.urionlinejudge.com.br/judge/pt/problems/view/1012

ÁREA
'''
x = input()
pi = 3.14159

valores = x.split() #Quebra os valores separados por espaço da variável anterior, x

A = float(valores[0])
B = float(valores[1])
C = float(valores[2])


a1 = (A * C) / 2    #a) a área do triângulo retângulo que tem A por base e C por altura. 

b2 = pi * (C ** 2)  #b) área do círculo de raio C. (pi = 3.14159)

c3 = (A + B) * C / 2   #c) área do trapézio que tem A e B por bases e C por altura.

d4 = B ** 2    #d) área do quadrado que tem lado B.

e5 = A * B   #e) área do retângulo que tem lados A e B.

print('TRIANGULO: {:.3f}' .format(a1))
print('CIRCULO: {:.3f}' .format(b2))
print('TRAPEZIO: {:.3f}' .format(c3))
print('QUADRADO: {:.3f}' .format(d4))
print('RETANGULO: {:.3f}' .format(e5))

#print(': {:.3f}' .format())