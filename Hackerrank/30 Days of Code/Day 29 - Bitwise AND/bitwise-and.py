#!/bin/python3

import sys

nTests = int(input().strip())
for _ in range(nTests):
    n, k = input().strip().split(' ')
    n, k = [int(n),int(k)]
    maxAB = 0
    for A in range(1, n):
        for B in range(A+1, n+1):
            val = A & B
            if val > maxAB and val < k:
                maxAB = val
    print(maxAB)
