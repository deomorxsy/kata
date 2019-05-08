def greet(name):
	if name == "Johnny":
		return "Hello, my love!"

	else:
		return "Hello, {name}!".format(name=name)

'''
another clever solution:

def greet(name):
    return "Hello, {name}!".format(name = ('my love' if name == 'Johnny' else name));

'''