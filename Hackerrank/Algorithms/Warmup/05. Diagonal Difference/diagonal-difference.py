#!/bin/python3

import sys

def diagonal_difference(N, a):
    primary_diagonal = sum([a[i+(N*i)] for i in range(N)])
    secondary_diagonal = sum([a[i+(N*(N-1-i))] for i in range(N)])
    return abs(primary_diagonal - secondary_diagonal)

n = int(input().strip())
a = []
for a_i in range(n):
    [a.append(int(a_temp)) for a_temp in input().strip().split(' ')]
print(diagonal_difference(n, a))
