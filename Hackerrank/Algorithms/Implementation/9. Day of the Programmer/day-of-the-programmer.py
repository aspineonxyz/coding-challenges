#!/bin/python3

import sys

class RussianCalendar(object):
  def __init__(self, year):
    if year < 1700 or year > 2700:
      raise ValueError
    self.year = year
    self.months = {
      1: 31,
      2: 15 if year == 1918 else 29 if self.is_leap_year() else 28,
      3: 31,
      4: 30,
      5: 31,
      6: 30,
      7: 31,
      8: 31,
      9: 30,
      10: 31,
      11: 30,
      12: 31,
    }

  def is_leap_year(self):
    if self.year > 1918 and self.year % 100 == 0:
        return self.year % 400 == 0
    return self.year % 4 == 0

  def find_256th(self):
    day, i = 0, 1
    while day + self.months[i] < 256:
      day += self.months[i]
      i += 1
    return str(256 - day).zfill(2) + '.' + str(i).zfill(2) + '.' + str(self.year)

def main():
  year = int(input().strip())
  r_cal = RussianCalendar(year)
  print(r_cal.find_256th())

if __name__ == '__main__':
  main()
