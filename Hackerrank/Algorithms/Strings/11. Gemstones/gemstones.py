#!/bin/python3

import sys

def gemstones(arr):
    setlist = [set(a) for a in arr]
    gems = set.intersection(*setlist)
    return len(gems)

def main():
    n = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
        arr_t = str(input().strip())
        arr.append(arr_t)
    print(gemstones(arr))

if __name__ == '__main__':
    main()
