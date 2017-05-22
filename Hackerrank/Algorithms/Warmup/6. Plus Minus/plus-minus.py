#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
signs = {'+': 0, '-': 0, '0': 0}
for i in arr:
    if i > 0:
        signs['+'] += 1
    elif i < 0:
        signs['-'] += 1
    else:
        signs['0'] += 1
print('{0:.6f}'.format(signs['+']/float(len(arr))))
print('{0:.6f}'.format(signs['-']/float(len(arr))))
print('{0:.6f}'.format(signs['0']/float(len(arr))))    
