#! usr/bin/env/python3

def lovefunc( flower1, flower2 ):
    return True if (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower1 % 2 != 0 and flower2 % 2 == 0) else False


'''
def lovefunc( flower1, flower2 ):
    if flower1 % 2 != 0 and flower2 % 2 == 0 or flower1 % 2 == 0 and flower2 % 2 != 0:
    	return True

    else:
    	return False

'''

'''
#Autor: deomorxsy
#Data: 05/03/2019

/// Opposites Attract - jbarget

https://www.codewars.com/kata/opposites-attract/train/python
'''