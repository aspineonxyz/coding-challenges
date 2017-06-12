b_num = bin(int(input()))[2:]
count, max_ones = 0, 0
for b in range(len(b_num)):
    if b_num[b] == '1':
        count += 1
    else:
        if count > max_ones:
            max_ones = count
        count = 0
print(max_ones if max_ones > count else count)
