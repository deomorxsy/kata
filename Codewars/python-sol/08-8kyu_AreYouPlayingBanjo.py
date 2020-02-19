#! usr/bin/env/python3

def areYouPlayingBanjo(name):
    #Linha 7 - Já que iniciais maiúsculas ou minúsculas não importam,
    #colocamos todas em maíusculas para facilitar.

    y = name.upper() 
    if y[0] == 'R':
    	return name + " plays banjo" 
    
    else:
    	return name + " does not play banjo"

if '__name__' == '__main__':
	main()
'''
#Autor: deomorxsy
#Data: 16/02/2019

/// Are You Playing Banjo? - MRodalgaard

https://www.codewars.com/kata/are-you-playing-banjo/train/python
'''