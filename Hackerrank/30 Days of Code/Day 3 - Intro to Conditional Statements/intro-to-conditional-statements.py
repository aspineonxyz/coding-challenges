N = int(input())
print("Not Weird" if N % 2 == 0 and (N <= 4 or N >= 22) else "Weird")
