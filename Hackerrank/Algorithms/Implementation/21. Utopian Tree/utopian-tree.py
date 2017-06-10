#!/bin/python3

import sys

def utopian_growth(phases):
  height = 1 # Height starts at 1m
  for i in range(phases):
    if i % 2 == 0:
      # spring - grow by doubling height
      height *= 2
    else:
      # summer - grow by 1m
      height += 1
  return height

def main():
  t = int(input().strip())
  for a0 in range(t):
    phases = int(input().strip())
    print(utopian_growth(phases))

if __name__ == "__main__":
  main()
