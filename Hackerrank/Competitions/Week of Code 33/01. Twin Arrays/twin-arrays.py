# Will either be:
# - min of A + min of B
# - min of A + second min of B
# - second min of A + min of B

def min_val(A, B):
  if A[0][1] != B[0][1]:
    return A[0][0] + B[0][0]
  else:
    return min(A[1][0] + B[0][0], A[0][0] + B[1][0])

def main():
  n = int(input().strip())
  A = [(int(a), i) for i, a in enumerate(input().strip().split(' '))]
  A = sorted(A, key=lambda x: x[0])
  B = [(int(b), i) for i, b in enumerate(input().strip().split(' '))]
  B = sorted(B, key=lambda x: x[0])
  print(min_val(A, B))

if __name__ == "__main__":
  main()
