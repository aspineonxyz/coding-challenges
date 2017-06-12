from array import *

N = int(input())
arr = array('i', [int(i) for i in input().split()])
arr.reverse()
[print(str(i)+" ",end="") for i in arr]
