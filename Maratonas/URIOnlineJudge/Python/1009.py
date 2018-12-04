#!usr/bin/env python3

'''
Iniciante
Problema 1009 do URI Online Judge
https://www.urionlinejudge.com.br/judge/pt/problems/view/1009
'''
# Linha 12: Nome(String), Salário Fixo(Float), Total de Vendas(Float) * Porcentagem de Comissão
# Linha 13: Aqui uso a função .format para substituir a variável entre as Chaves, e o índice 1
#			que equivale ao índice do resultado da Operação.

x = input(), float(input()) + (float(input()) * 0.15)
print('TOTAL = R$ {:.2f}' .format(x[1])) 