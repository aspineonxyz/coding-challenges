#!/bin/python3

import sys

def min_magic(max_height, heights):
  idx = 0
  min_magic = 0
  while idx < len(heights):
    if heights[idx] > max_height:
      min_magic += 1
      max_height += 1
    else:
      idx += 1
  return min_magic

def main():
  n, k = map(int, input().strip().split(' '))
  heights = list(map(int, input().strip().split(' ')))
  print(min_magic(k, heights))

if __name__ == "__main__":
  main()
