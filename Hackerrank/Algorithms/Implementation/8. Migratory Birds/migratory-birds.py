#!/bin/python3

import sys
from collections import Counter

def most_popular_birds(bird_types) -> int:
  c = Counter(bird_types)
  c_max = max(c.values())
  return min([key for (key, value) in c.items() if value == c_max])

def main():
  n = int(input().strip())
  bird_types = list(map(int, input().strip().split(' ')))
  print(most_popular_birds(bird_types))

if __name__ == '__main__':
  main()
