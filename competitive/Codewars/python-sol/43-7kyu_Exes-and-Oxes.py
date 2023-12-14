def xo(s):
	#using strings and .join() as principal 
	x_list = ''
	o_list = ''
	for i in range(len(s)):
		if s[i] == 'x' or s[i] == 'X': # case-insensitive?
			x_list += x_list.join(s[i]) 
		elif s[i] == 'o' or s[i] == 'O': # case-insensitive?
			o_list += o_list.join(s[i]) 
		# make sure to add the '+=' operator or similar. .join() is different from .format()!

	if len(x_list) == len(o_list):
		return True
	else:
		return False

'''
def xo(s):
	x_list = []
	o_list = []
	for i in range(len(s)):
		if s[i] == 'x' or s[i] == 'X': # case-insensitive
			x_list.append(s[i]) 
		elif s[i] == 'o'or s[i] == 'O': # case-insensitive
			o_list.append(s[i])

	if len(x_list) == len(o_list):
		return True
	elif len(x_list) != len(o_list):
		return False
	else:
		return True
'''