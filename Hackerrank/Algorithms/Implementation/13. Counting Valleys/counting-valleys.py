def count_valleys(steps):
  valleys = 0
  height = 0
  for s in steps:
    if s == 'U':
      height += 1
      if height == 0:
        valleys += 1
    else:
      height -= 1
  return valleys

n = int(input().strip())
steps = list(input().strip())
print(count_valleys(steps))
