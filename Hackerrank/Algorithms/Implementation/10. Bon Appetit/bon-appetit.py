def bill_split(c, b_charged, K):
  if sum(c) / 2 == b_charged:
    return int(c[K] / 2)
  else:
    return 'Bon Appetit'

def main():
  n, K = map(int, input().strip().split())
  c = list(map(int, input().strip().split()))
  b_charged = int(input().strip())
  print(bill_split(c, b_charged, K))

if __name__ == '__main__':
  main()
