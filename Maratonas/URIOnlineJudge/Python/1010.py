#!usr/bin/env python3

'''
Iniciante
Problema 1010 do URI Online Judge
https://www.urionlinejudge.com.br/judge/pt/problems/view/1010

'''

x = input(), input()

peça1 = x[0] #Separa o primeiro comando input() do segundo, chamando o primeiro índice 0
peça1 = peça1.split() #Atualiza a variável peça1 pra que guarde a lista criada por .SPLIT()

total_peça1 = float(int(peça1[1]) * float(peça1[2])) 
	#Produto do NÚMERO DE PEÇAS em INT por o PREÇO DE PEÇAS em FLOAT.
	#O valor final deve ser Float também!


peça2 = x[1] #Separa o segundo comando input() do primeiro, chamando o segundo índice 1
peça2 = peça2.split() #Atualiza a variável peça2 pra que guarde a lista criada por .SPLIT()

total_peça2 = float(int(peça2[1]) * float(peça2[2]))
	#Produto do NÚMERO DE PEÇAS em INT por o PREÇO DE PEÇAS em FLOAT.
	#O valor final deve ser Float também, então tem que converter novamente!

print('VALOR A PAGAR: R$ {:.2f}' .format(total_peça1 + total_peça2))