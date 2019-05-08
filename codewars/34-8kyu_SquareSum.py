def square_sum(numbers):
    '''
    In line 9 we use the list method .append() to add the result of the operation inside
    the empty list. Test bugs in the code with the 'Debugger' in line 10.
    Line 13 is the calling to run the script in a terminal.
    '''
    var = []
    for i in numbers:
    	var.append(i ** 2)
    	print(var) #DEBUGGER
    return sum(var)

print(square_sum([1, 2, 2]))#DEBUGGER

'''List Comprehensions
return sum(i ** 2 for i in numbers)'''