#!/bin/python3

import sys

def min_magic_cost(square):
  min_magic_cost = 100
  solutions = [[8,1,6,3,5,7,4,9,2],
               [6,1,8,7,5,3,2,9,4],
               [4,9,2,3,5,7,8,1,6],
               [2,9,4,7,5,3,6,1,8],
               [8,3,4,1,5,9,6,7,2],
               [4,3,8,9,5,1,2,7,6],
               [6,7,2,1,5,9,8,3,4],
               [2,7,6,9,5,1,4,3,8]
              ];
  for magic_square in solutions:
    cost = 0
    for i in range(9):
      if magic_square[i] != square[i]:
        cost += abs(magic_square[i] - square[i])
    if cost < min_magic_cost:
      min_magic_cost = cost
  return min_magic_cost

square = []
for s in range(3):
  [square.append(int(s)) for s in input().strip().split(' ')]
print(min_magic_cost(square))
