mySet_1 = set(map(int, input().split()))
mySet_2 = set(map(int, input().split()))
print(*sorted(mySet_1 & mySet_2), end='')
