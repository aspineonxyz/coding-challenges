#!/bin/python3

import sys

def mini_max(arr):
  total = sum(arr)
  return str(total - max(arr)) + ' ' + str(total - min(arr))

arr = list(map(int, input().strip().split(' ')))

print(mini_max(arr))
