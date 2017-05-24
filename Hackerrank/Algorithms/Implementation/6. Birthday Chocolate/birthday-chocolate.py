#!/bin/python3

import sys

def solve(n, s, d, m):
  if m > n:
    return 0
  count = 0
  for i in range(n + 1 - m):
    if sum(s[i:i+m]) == d:
      count += 1
  return count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = map(int, input().strip().split(' '))
print(solve(n, s, d, m))
