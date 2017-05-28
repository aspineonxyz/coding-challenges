#!/bin/python3

import sys
from math import sqrt

def factors(n):
    results = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            results.add(i)
            results.add(int(n / i))
    return results

def getTotalX(a, b):
  b_factors = factors(b[0])
  for i in range(1, len(b)):
    b_factors = b_factors & factors(b[i])
  count = 0
  for i in b_factors:
    between_both = True
    for j in a:
      if i % j != 0:
        between_both = False
        break
    if between_both:
      count += 1
  return count

n, m = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
print(getTotalX(a, b))
