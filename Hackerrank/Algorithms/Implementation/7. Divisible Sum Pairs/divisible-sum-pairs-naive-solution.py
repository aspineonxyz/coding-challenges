#!/bin/python3

import sys

def div_sum_pairs(arr, k) -> int:
  count = {}
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if (arr[i] + arr[j]) % k == 0:
        count[frozenset([i, j])] = 1
  return sum(count.values())

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))

print(div_sum_pairs(a, k))
