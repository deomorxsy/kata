#! usr/bin/env/python3

def main():
	#BUSCA - Identificar de vogais
	word, letter = input(), input()
	index = 0

	while index < len(word): #ENQUANTO o index 0 for menor que a extensão de todas as palavras da var. word
		if word[index] == letter: #SE o seguinte index, presente em word, for igual a letter,
			return print('Sim, aparece!')
		else:
			return(print('Não aparece!'))
		index += 1 #Atualizando o index, assim, quando chegar em len(word) o programa parará
	return-1 #Quando o index 0 não for menor, retorne -1

if __name__ == '__main__':
	main()

'''
Autor: deomorxsy
Data: 21/01/2019

PARTE 2
/// Exercícios com Strings nº 07 do Python Wiki BR
https://wiki.python.org.br/ExerciciosComStrings
'''