#!usr/bin/env/python3

# 7kyu Kata. List Filtering
# Check at https://www.codewars.com/kata/53dbd5315a3c69eed20002dd


# With List Comprehensions and isinstance() built-in method.

def filter_list(l):
	'return a new list with the strings filtered out'
	return [l[i] for i in range(len(l)) if isinstance(l[i], int)]