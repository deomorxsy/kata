#! usr/bin/env/python3

def remove_char(s):
	#Na linha 6 'var' servirá para o Slice de índices.

    var = (len(s) - 1) 
    return s[1:var] #No lugar de 'var' poderia ser apenas -1.

if '__name__' == '__main__':
	main()

'''
#Autor: deomorxsy
#Data: 14/02/2019

/// Remove First and Last Character - Steadyx

https://www.codewars.com/kata/remove-first-and-last-character/train/python
'''