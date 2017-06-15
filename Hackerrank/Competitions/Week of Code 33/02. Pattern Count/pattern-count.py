#!/bin/python3

import re

def patternCount(s):
    return len([m.start() for m in re.finditer('(?=(1{1}0{1,}1{1}))', s)])

def main():
  q = int(input().strip())
  match_counts = []
  for _ in range(q):
    match_counts.append(patternCount(input().strip()))
  for count in match_counts:
    print(count)

if __name__ == "__main__":
  main()
