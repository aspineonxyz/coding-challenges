#!/bin/python3

import sys

def money_spent(savings, keyboards, drives):
  max_spent = -1
  for k in keyboards:
    for d in drives:
      spent = k + d
      if spent <= savings and spent > max_spent:
        max_spent = spent
  return max_spent

def main():
  savings, n, m = map(int, input().strip().split(' '))
  keyboards = list(map(int, input().strip().split(' ')))
  drives = list(map(int, input().strip().split(' ')))

  print(money_spent(savings, keyboards, drives))

if __name__ == '__main__':
  main()
