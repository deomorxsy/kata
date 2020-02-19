def count_sheeps(arrayOfSheeps):
	# TODO May the force be with you
	contador = 0
	for i in arrayOfSheeps:
		if i == True:
			contador = contador + 1
	return contador


#list comprehensions:

return (lambda contador: contador + 1 for i in arrayOfSheeps if i == True)