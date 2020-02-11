def accum(s):
	# your code
	acc = ''
	for i in range(len(s)):
		if i == s[0]:
			acc += acc.join(s[0].upper()) + '-'
		acc += acc.join(s[i].upper()) + (str(s[i].lower() * i) + '-')
	return acc[:len(acc) - 1]

#accum('ZpglnRxqenU')