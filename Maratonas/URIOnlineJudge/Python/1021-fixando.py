#! usr/bin/env/python3

'''
Iniciante
Problema 1021 do URI Online Judge
https://www.urionlinejudge.com.br/judge/pt/problems/view/1021

Notas e Moedas
'''

def main():
    from decimal import Decimal as D

    x = D(input()) #+ 0.001          # valor monetário


    if (0 <= x <= 1000000.00):

        # NOTAS
        print('NOTAS:')

        print('{} nota(s) de R$ 100.00' .format(int(x / 100)))
        x %= 100

        print('{} nota(s) de R$ 50.00' .format(int(x / 50)))
        x %= 50

        print('{} nota(s) de R$ 20.00' .format(int(x / 20)))
        x %= 20

        print('{} nota(s) de R$ 10.00' .format(int(x / 10)))
        x %= 10

        print('{} nota(s) de R$ 5.00' .format(int(x / 5)))
        x %= 5

        print('{} nota(s) de R$ 2.00' .format(int(x / 2)))
        x %= 2

        # MOEDAS
        print('MOEDAS:')

        print('{} moeda(s) de R$ 1.00' .format(int(x / 1)))
        x %= 1

        print('{} moeda(s) de R$ 0.50' .format(int(x / D(0.5))))
        x %= D(0.5)

        print('{} moeda(s) de R$ 0.25' .format(int(x / D(0.25))))
        x %= D(0.25)

        print('{} moeda(s) de R$ 0.10' .format(int(x / D(0.10))))
        x %= D(0.10)

        print('{} moeda(s) de R$ 0.05' .format(int(x / D(0.05))))
        x %= D(0.05)

        print('{} moeda(s) de R$ 0.01' .format(int(x / D(0.01) + D(0.01))))

        #print(Decimal(x))




if __name__ == ('__main__'):
    main()