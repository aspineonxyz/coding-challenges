arr = []
for _ in range(6):
    arr.append([int(num) for num in input().split()])

max_hourglass = max([arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2]
                     [j] + arr[i + 2][j + 1] + arr[i + 2][j + 2] for i in range(4) for j in range(4)])

print(max_hourglass)
