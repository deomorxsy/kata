#!usr/bin/env/python3

def score(dice):
	# your code here
	aux_one = ''
	aux_two = ''
	aux_three = ''
	aux_four = ''
	aux_five = ''
	aux_six = ''

	for i in range(len(dice)):
		if dice[i] == 1:
			aux_one += '1'

		elif dice[i] == 2:
			aux_two += '1'

		elif dice[i] == 3:
			aux_three += '1'

		elif dice[i] == 4:
			aux_four += '1'

		elif dice[i] == 5:
			aux_five += '1'

		elif dice[i] == 6:
			aux_six += '1'

	return [1000 if aux_one == '111' else  100 if aux_one == '1' or 600 if aux_six == '666' or 500 if aux_five == '555' else 50 if aux_five == '5' or 400 if aux_four == '444' or 300 if aux_three == '333' or 200 if aux_two == '222']

