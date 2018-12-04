#!/usr/bin/env python3

'''
#2018-07-29
#@deomorxsy
Função que determina se o ano do input é Bissexto ou não.
'''

def is_leap(year):
	if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
		return True
	return False

#tests
print(is_leap(2000))
print(is_leap(2100))
print(is_leap(1900))

'''
ANALISAR: Resposta do StackOverflow (https://stackoverflow.com/questions/11621740/how-to-determine-whether-a-year-is-a-leap-year)


=========

OUTRO MODO DE ESCREVER ESSA FUNÇÃO: DIRETO NO RETURN.

def is_leap(year):
    """Determina qual ano é um ano bissexto."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

'''