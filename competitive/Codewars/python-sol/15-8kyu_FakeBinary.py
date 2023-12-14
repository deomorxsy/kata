def fake_bin(x):
	var = ''
	for i in x:
		if int(i) < 5:
			var += '0'
		else:
			var += '1'
	return var

#o principal do código acima é de fato a variável '', a qual será atribuída os 0s e 1s.
#Veja abaixo em compreensão de lista:

'''
def fake_bin(x):
    return ''.join('0' if i < '5' else '1' for i in x)

 #07/03
 '''