#! usr/bin/env/python3

def bonus_time(salary, bonus):
	#QUESTIONAMENTO:
	#Como se chama o bloco abaixo? Compreensão de Lista? Mas não é uma lista!
	# É String?! -- Pesquise!
	
    return ('${}' .format(int(salary) * (10 if float(bonus) == True else 1)))