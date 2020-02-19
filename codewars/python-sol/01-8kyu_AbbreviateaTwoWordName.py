#! usr/bin/env/python3

def abbrevName(name):
    fname, surename = name.split()
    x = ('{}.{}' .format(fname[0], surename[0]))
    return x.upper()

if '__name__' ==  '__main__':
    main()

'''
#Autor: deomorxsy
#Data: 09/02/2019

/// Abbreviate a Two Word Name - samjam48

https://www.codewars.com/kata/abbreviate-a-two-word-name/train/python
'''







