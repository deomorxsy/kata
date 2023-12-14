#Faça um Programa que calcule a área de um quadrado, em seguida
#mostre o dobro desta área para o usuário.

l = int(input('Digite o Lado do Quadrado: '))

aq = l ** 2

aq *= 2

print('Área do Quadrado =', (aq//2))
print('Dobro da Área =', aq)