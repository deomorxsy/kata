#!usr/bin/env/python3

# 7kyu Kata. List Filtering
# Check at https://www.codewars.com/kata/53dbd5315a3c69eed20002dd


# Now without while indented to the For Loop, using isinstance() built-in method.

def filter_list(l):
	'return a new list with the strings filtered out'
	#based on the previous code using isinstance() built-in method:
	#return [l[i] for i in range(len(l)) if isinstance(l[i], int)]
	newlist = []
	for i in range(len(l)):
		if isinstance(l[i], int): # Se a afirmação de que o tipo de dado é INT é verdadeira.
			newlist.append(int('{}'.format(l[i])))
	return newlist