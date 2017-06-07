#!/bin/python3

import sys

def rankings(scores, alice):
  # get the unique scores
  unique_scores = [scores[0]]
  for s in scores:
    if s != unique_scores[-1]:
      unique_scores.append(s)
  # set rank to last place
  rank = len(unique_scores)
  # loop through alices scores
  for a in alice:
    while a > unique_scores[rank - 1] and rank > 0:
      # alice scored better than a score, increase her rank by 1
      rank -= 1

    if a == unique_scores[rank - 1]:
      # alice tied with a score print her rank
      print(rank)
    else:
      # alice just didn't beat the next score, print rank + 1
      print(rank + 1)

def main():
  n = int(input().strip())
  scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
  m = int(input().strip())
  alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
  rankings(scores, alice)

if __name__ == '__main__':
  main()
