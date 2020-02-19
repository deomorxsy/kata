#!usr/bin/env/python3
# 8kyu Kata. What's the real floor?
# Check at https://www.codewars.com/kata/574b3b1599d8f897470018f6/train/python

def get_real_floor(n):
# conditionals
	if n <= 0:
		return n
	elif n < 13:
		return n-1
	elif n > 13:
		return n-2

'''
1 0
2 1
3 2
4 3
5 4
6 5
7 6
8 7
9 8
10 9
11 10
12 11
X  ?? (12)
14 12 (13)
15 13 (14)
'''