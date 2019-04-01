#! usr/bin/env/python3

def getCount(inputStr):
    num_vowels = 0
    vowels = 'aiueo'
    #Para cada índice em inputStr, se índice estiver dentro de Vowels, some 1 ao número de vowels.
    for i in inputStr:
        if i in vowels: #aqui vowels poderia ser apenas a string 'aiueo'
            num_vowels += 1
    return num_vowels

if '__name__' == '__main__':
	main()

#07/03