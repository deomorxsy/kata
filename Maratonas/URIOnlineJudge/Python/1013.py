#!usr/bin/env python3

'''
Iniciante
Problema 1013 do URI Online Judge
https://www.urionlinejudge.com.br/judge/pt/problems/view/1013

O Maior
'''

def main ():
	'''
	Lê três números Inteiros e diz qual é o maior entre eles.
	'''
	a,b,c = [int(i) for i in input().split()]
	print('{} eh o maior' .format(max(a,b,c)))


if __name__ == '__main__':
	main()