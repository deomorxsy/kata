def reverse_seq(n):
    return [ i for i in range(n+1)[:0:-1] ]

'''
here I use list comprehensions to reduce the size of the code.
thus the return line doesn't need to return a variable who holds an list,
because we can transform all the instructions in a list itself with the brackets [].

the range function puts n+1 as its range, who will print '0,1,2,3,4,5'.
We want all of them but the first index, '0'; to fix it we use LIST SLICING [:0:-1].

#PS:The brackets are spaced to facilitate the reading
'''