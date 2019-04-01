def to_camel_case(text):
    #your code here
    #return [i.strip('-' and '_') for i in text]
    alto = 0
    for i in text:
    	if i == '-' or '_':
    		alto = text.find('-' or '_') + 1
    		text[alto].upper()