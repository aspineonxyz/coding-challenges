#!/bin/python3

import sys

def div_sum_pairs(arr, k) -> int:
  count = 0
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if (arr[i] + arr[j]) % k == 0:
        count += 1
  return count

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))

print(div_sum_pairs(a, k))
