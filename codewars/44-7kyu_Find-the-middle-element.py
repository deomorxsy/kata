#wrong

def gimme(l):
    # Implement this function
	if (l[0] >= l[1]) and  (l[0] <= l[2]) or (l[0] <= l[1] and l[0] >= l[2]):
		return 0

	if (l[1] >= l[0]) and  (l[1] <= l[2]) or (l[1] <= l[0] and l[0] >= l[2]):
		return 1

	if (l[2] >= l[0]) and  (l[2] <= l[1]) or (l[2] <= l[0] and l[2] >= l[1]):
		return 2
