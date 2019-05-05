myList = list(map(int, input().split()))
for i in range(0, len(myList) - 1):
    if myList[i + 1] > myList[i]:
        print(myList[i + 1], end=' ')
