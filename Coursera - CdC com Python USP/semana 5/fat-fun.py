#!/usr/bin/env python3
'''
Paixão, L.
2018-07-01

Coursera - Semana 5: Funções (Definição, criação e utilização de funções. Escopo de variável.)
Panda IME - Exercício 6.2
'''
#Função Fatorial
def fat(n):
    r = 1
    for fat in range(n,0,-1): #For range que fará um Loop fatorial de n até 1, de -1 em -1.
        r *= fat
        print(fat, '!')

        if fat == 1: #Se fat = 1 for True, então o Loop estará encerrado.
            print('Your count is finished!')
            print('The Fatorial value is', r,'.')
    return r


#...Que será ativada pelo número escolhido pelo usuário abaixo.
n = int(input('Digite um número: '))
#teste
print(n,'! =', fat(n))


# testes
#print("0! =", fat(0))
#print("1! =", fat(1))
#print("5! =", fat(5))
#print("17! =", fat(17))


