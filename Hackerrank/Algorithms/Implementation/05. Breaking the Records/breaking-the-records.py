#!/bin/python3

import sys

def getRecord(scores):
  most, least = scores[0], scores[0]
  highest_score, lowest_score = 0, 0
  for s in scores:
    if s > most:
      most = s
      highest_score += 1
    elif s < least:
      least = s
      lowest_score += 1
  return [highest_score, lowest_score]

n = int(input().strip())
scores = list(map(int, input().strip().split(' ')))
result = getRecord(scores)
print (" ".join(map(str, result)))
