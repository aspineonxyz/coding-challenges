from math import sqrt, ceil

def prime(n):
    if n == 2:
        return "Prime"
    if n == 1 or n % 2 == 0:
        return "Not prime"
    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return "Not prime"
    return "Prime"

for _ in range(int(input())):
    print(prime(int(input())))
