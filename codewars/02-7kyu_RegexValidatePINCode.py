#! usr/bin/env/python3

#Código incompleto/EDIT

def validate_pin(pin):
    num = ['1','2','3','4','5','6','7','8','9','0']
    index = 0
    #indexPin
    
    if len(pin) == (4 or 6):
        if pin[index] in num:
            index += 1
            return True
        else:
            return False
    else:
        return False


if '__name__' == '__main__':
    main()
        
        

'''
#Autor: deomorxsy
#Data: 09/02/2019

/// Regex validate PIN code - JMurphyWeb [EDIT]

https://www.codewars.com/kata/regex-validate-pin-code/
'''       

      