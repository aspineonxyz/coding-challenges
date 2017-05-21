s,t = map(int,input().strip().split(' '))
apple_tree, orange_tree = map(int,input().strip().split(' '))
n_apples, n_oranges = map(int,input().strip().split(' '))
apples = [int(apple) for apple in input().strip().split(' ')]
oranges = [int(orange) for orange in input().strip().split(' ')]

print(sum([1 for apple in apples if (apple_tree + apple) >= s and (apple_tree + apple) <= t]))
print(sum([1 for orange in oranges if (orange_tree + orange) >= s and (orange_tree + orange) <= t]))
