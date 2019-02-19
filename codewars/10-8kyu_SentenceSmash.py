#! usr/bin/env/python3

def smash(words):
	index = 0
	newstr = ''
	for x in words:
		newstr += words[index] + ''
		index += 1
	return newstr
