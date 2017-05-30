#!/bin/python3

import sys

def cats_and_a_mouse(x,y,z):
  if abs(x-z) < abs(y-z):
    return "Cat A"
  elif abs(x-z) > abs(y-z):
    return "Cat B"
  else:
    return "Mouse C"

def main():
  q = int(input().strip())
  for a0 in range(q):
    x,y,z = map(int, input().strip().split(' '))
    print(cats_and_a_mouse(x,y,z))

if __name__ == '__main__':
  main()
