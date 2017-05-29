#!/bin/python3

import sys

def min_page_turns(n, p):
  forward = p / 2
  backward = (n - p + 1) / 2 if n % 2 == 0 else (n - p) / 2
  return int(forward if forward < backward else backward)

def main():
  n = int(input().strip())
  p = int(input().strip())
  print(min_page_turns(n, p))

if __name__ == '__main__':
  main()
