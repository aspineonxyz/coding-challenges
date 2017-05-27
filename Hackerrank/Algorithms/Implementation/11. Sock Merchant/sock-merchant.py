#!/bin/python3

import sys
from collections import Counter

def matching_pairs(socks):
  sock_count = Counter(socks)
  pairs = 0
  for s in sock_count.values():
      pairs += int(s / 2)
  return pairs

def main():
  n = int(input().strip())
  socks = list(map(int, input().strip().split()))
  print(matching_pairs(socks))

if __name__ == '__main__':
  main()
