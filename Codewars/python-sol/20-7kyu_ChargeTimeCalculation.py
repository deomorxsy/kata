#UNSOLVED

def calculate_time(battery,charger):
	#your code here
	if battery >= 0 and battery <= 85:
		return print((battery * 0.85) / (charger))

	elif battery >= 85 and battery <= 95:
		return print((battery * 0.10) / (charger))

	else:
		return print((battery * 0.5) / (charger))

calculate_time(1000, 500)