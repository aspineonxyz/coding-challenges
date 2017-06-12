import sys
phone_book = {}
for _ in range(int(input())):
    name, number = input().split()
    phone_book[name] = number
for line in sys.stdin:
    name = line.strip()
    if name in phone_book:
        print('{}={}'.format(name, phone_book[name]))
    else:
        print('Not found')
