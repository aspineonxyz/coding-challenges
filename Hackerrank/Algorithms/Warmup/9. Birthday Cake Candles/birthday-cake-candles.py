#!/bin/python3

import sys

def candles_blown(n, heights):
  max_height = 0
  count = 0
  for h in heights:
    if h > max_height:
      max_height = h
      count = 1
    elif h == max_height:
      count += 1
  return count

n = int(input().strip())
heights = [int(height_temp) for height_temp in input().strip().split(' ')]

print(candles_blown(n, heights))
