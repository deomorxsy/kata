#! usr/bin/env/python3

def solution(string):
    return string[::-1]


if '__name__' == '__main__':
	main()

	#Perceba que o Slicing é basicamente 3S: 'start:stop:steps'.
    #Na linha 4, não especificar start e stop quer dizer que a String vai rodar
    #como ela foi informada. Se o step for mudado para -1,
    #os índices serão mostrados '-1 por -1'.

'''
#Autor: deomorxsy
#Data: 14/02/2019

/// Reversed Strings - jhoffner

https://www.codewars.com/kata/reversed-strings/train/python
'''