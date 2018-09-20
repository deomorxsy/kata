#!/usr/bin/env python3

def test(n):
    r = 1
    while n >= 0:
        r *= n
        print(n)
        n -= 1
        if n == 1:
            print('Fatorial =', r)
            break

test(5)
