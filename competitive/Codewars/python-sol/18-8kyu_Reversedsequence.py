def reverse_seq(n):
	list = []
	for i in range(n+1)[:0:-1]:
		list.append(i)
	return list

#basic of list slicing: [start:stop:steps]. Append adds an item to the list
#up there the stop is 0 (until 1) and the steps is -1.
'''
also the range function with n+1 is needed because the atribute of range is (stop)
so if 'n = 5',the 
 'for in range(n)' will print >>>'0, 1, 2, 3, 4'.

To print all of them, we have to sum n+1.
 'n = 6' will print >>> '0, 1, 2, 3, 4, 5'

But we want '1,2,3,4,5', so we fix it with the LIST SLICING [:0:-1],
already explained in line 7.