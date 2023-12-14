def array_madness(a,b):
	# Ready, get, set, GO!!!
	#IF a soma dos quadrados de 'a' for maior que a soma dos cubos de 'b', return TRUE
	return sum(i**2 for i in a) > sum(i**3 for i in b)

print(array_madness([4,5,6], [1,2,3]))