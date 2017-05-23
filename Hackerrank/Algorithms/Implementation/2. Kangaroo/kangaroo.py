#!/bin/python3

import sys

def kangaroos(x1, v1, x2, v2):
  if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
    return "YES"
  else:
    return "NO"

x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

print(kangaroos(x1, v1, x2, v2))
