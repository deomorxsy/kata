def basic_op(operator, value1, value2):
    #your code here +, -, *, /
    if operator == '+':
    	return value1 + value2
    if operator == '-':
    	return value1 - value2
    if operator == '*':
    	return value1 * value2
    if operator == '/':
    	return value1 / value2

return ((value1 + value2) if operator == '+' else (value1 - value2) if operator == '-' else (value1 * value2) if operator == '*' else (value1 / value2) if operator == '/')