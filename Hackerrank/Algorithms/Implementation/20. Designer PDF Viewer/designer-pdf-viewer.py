#!/bin/python3

import string

def highlighted_area(word, heights):
  height = 0
  alphabet = string.ascii_letters
  for i in range(len(alphabet)):
    if alphabet[i] in word:
      if heights[i] > height:
        height = heights[i]
  return len(word) * height

def main():
  heights = list(map(int, input().strip().split(' ')))
  word = input().strip()
  print(highlighted_area(word, heights))

if __name__ == "__main__":
  main()
