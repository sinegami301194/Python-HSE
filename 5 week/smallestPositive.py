myList = list(map(int, input().split()))
min = 10000
for i in range(0, len(myList)):
    if myList[i] > 0:
        if myList[i] < min:
            min = myList[i]
print(min, end=' ')
