#! /usr/bin/env python3
'''
Paixão, L.
2018-07-01

Coursera - Semana 5: Funções (Definição, criação e utilização de funções. Escopo de variável.)
Exercício 1: Máximo entre dois
'''

def maximo(n,m):
    '''(int) -> int
    Recebe 2 números e retorna o maior deles

    '''
    if n >= m:
        return(n)

    else:
        if m >= n:
            return(m)


#testes
(maximo(3,4))
(maximo(0,-1))
(maximo(5,6))
(maximo(233,500))
(maximo(1000,111))
