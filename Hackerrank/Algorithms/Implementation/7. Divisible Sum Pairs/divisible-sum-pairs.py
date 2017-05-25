#!/bin/python3

import sys
from itertools import combinations

def div_sum_pairs(arr, k) -> int:
  pairs = combinations(arr, 2)
  count = 0
  while True:
    try:
      p = pairs.__next__()
      if (p[0] + p[1]) % k == 0:
        count += 1
    except StopIteration:
      break
  return count

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))

print(div_sum_pairs(a, k))
