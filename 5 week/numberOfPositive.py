myList = list(map(int, input().split()))
count = 0
for i in range(0, len(myList)):
    if myList[i] > 0:
        count += 1
print(count, end=' ')
