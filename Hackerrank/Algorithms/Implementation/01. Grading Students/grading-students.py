#!/bin/python3

import sys

def rounder(num, rounder):
  return int(rounder * round(float(num)/rounder))

def solve(grades):
  for i in range(len(grades)):
    if grades[i] < 38:
      continue
    g = rounder(grades[i], 5)
    if g > grades[i]:
      grades[i] = g
  return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
  grades_t = int(input().strip())
  grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
