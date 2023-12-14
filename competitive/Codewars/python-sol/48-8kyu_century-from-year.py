#!usr/bin/env/python3
# 8kyu Kata. Century From Year
# Check at https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python

def century(year):
	# Finish this :)
	if (year - 1) % 100 == 99:
		return (year // 100)
	else:
		return (year // 100) + 1