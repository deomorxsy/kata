#!/usr/bin/env python3

for fat in range(6,0,-1):
    r = 1
    r *= fat
    print(fat, '!')

    if fat == 1:
        break
    print('Your count is finished!')

