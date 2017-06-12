def bubble_sort(n, a):
    total_swaps = 0
    for _ in range(n):
        swaps_per_round = 0
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                tmp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = tmp
                swaps_per_round += 1
        if swaps_per_round == 0:
            break
        total_swaps += swaps_per_round
    print("Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}".format(total_swaps, a[0],a[len(a) - 1]))

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
bubble_sort(n, a)
