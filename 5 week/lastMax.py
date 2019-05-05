myList = list(map(int, input().split()))
max = 0
index = 0
for i in range(0, len(myList)):
    if myList[i] >= max:
        index = i
        max = myList[i]
print(max, index, end=' ')
