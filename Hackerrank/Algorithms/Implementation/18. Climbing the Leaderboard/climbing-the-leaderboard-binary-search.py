#!/bin/python3

import sys

"""
Search for the rank using binary search
"""
def ranking_binary_search(scores, start, end, alice) -> int:
  if alice < scores[end]:
    return len(scores)
  if alice >= scores[start]:
    return 0
  if end - start <= 1:
    return end
  mid = int((start + end) / 2)
  if scores[mid] < alice:
    return ranking_binary_search(scores, start, mid, alice)
  elif scores[mid] == alice:
    return mid;
  else:
    return ranking_binary_search(scores, mid, end, alice)

"""
Removes duplicates in a sorted list and returns the unique list in O(n)
"""
def remove_duplicates(items):
  unique_items = [items[0]]
  for item in items:
    if item != unique_items[-1]:
      # item isn't the same as the last added item, append item
      unique_items.append(item)
  return unique_items

"""
Print the rankings for each score player achieved
ASSUMPTIONS: Players score increases & scores are in decending order
"""
def print_rankings(all_scores, players_scores):
  # get the unique scores
  scores = remove_duplicates(all_scores)
  # loop through alices scores
  for player_score in players_scores:
    # print the rank
    print(ranking_binary_search(scores, 0, len(scores)-1, player_score) + 1)

def main():
  n = int(input().strip())
  scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
  m = int(input().strip())
  alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
  print_rankings(scores, alice)

if __name__ == '__main__':
  main()
