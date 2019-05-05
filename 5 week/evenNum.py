myList = list(map(int, input().split()))
for i in range(0, len(myList)):
    if myList[i] % 2 == 0:
        print(myList[i], end=' ')
