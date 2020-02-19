#!usr/bin/env/python3

# 7kyu Kata. List Filtering
# Check at https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

def filter_list(l):
	'return a new list with the strings filtered out'
	newlist = []
	# The target list, used to append the unwanted items
	nl_index = 0 # newlist index
	for i in range(len(l)): # OK
		if type(l[i]) == int: #OK
			newlist.append(l.pop(i)) #OK
			while nl_index < len(newlist):
				l.insert(i, newlist[nl_index]) # Insert the item from newlist in l, at the exact position it was removed from it previously with the .pop() method.
				nl_index += 1 # updates newlist's index
	return newlist # Must be indent in the same level of FOR. Otherwise, the LOOP doesn't work.


#filter_list([1,2,'a','b'])
'''
1st test:

>>> for i in range(len(l)):
...		if type(l[i]) == str:
...			newlist.append(l.pop(i))
...			l.insert(i, newlist[0])
...		print(newlist)

[]
[]
['a']
['a', 'b']

>>>
>>> l
[1, 2, 'a', 'a']

2nd test:
>>> while index < len(newlist):
...		index += 1
...		print(index)

0
1

---

3rd test. It'll return the list with STRINGS, but we want INTERGERS, so make sure to change the Class Type inside the If Conditional.

def filter_list(l):
	'return a new list with the strings filtered out'
	newlist = []
	# The target list, used to append the unwanted items
	nl_index = 0 # newlist index
	for i in range(len(l)): # OK
		if type(l[i]) == str: #OK
			newlist.append(l.pop(i)) #OK
			while nl_index < len(newlist):
				l.insert(i, newlist[nl_index]) # Insere o item da 'newlist' na posição do item que acabou de ser retirado anteriormente.
				nl_index += 1 # atualiza o index da newlist
	return newlist
'''