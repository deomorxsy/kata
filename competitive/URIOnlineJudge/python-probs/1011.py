#!usr/bin/env python3

'''
Iniciante
Problema 1011 do URI Online Judge
https://www.urionlinejudge.com.br/judge/pt/problems/view/1011

'''

r = float(input()) #Raio da Esfera
pi = 3.14159 #Valor de Pi aproximado

volume = float((4/3) * pi * (r ** 3)) #Cálculo do Volume da Esfera

print('VOLUME = {:.3f}' .format(volume)) #Injeta uma variável no : entre as chaves.