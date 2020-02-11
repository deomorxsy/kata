#!usr/bin/env/python3
# 6kyu Kata. Two Sum [WIP]
# Check at https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python

def two_sum(numbers, target):
	# start coding!
	acc = 0
	t1 = 
	for i in range(len(numbers)):
		print("item {}:".format(i))
		if target - numbers[acc] == numbers[i]:
			return (numbers[i], numbers[acc]) #returning a tuple
		acc += 1 #ends out of range, 3


	return (int("{}, {}".format())) for i in range(len(numbers)) if numbers[i] == target - numbers[acc]