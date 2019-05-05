myList = list(map(int, input().split()))
min = myList[0]
max = myList[0]
minIndex = 0
maxIndex = 0
for i in range(0, len(myList)):
    if myList[i] < min:
        min = myList[i]
        minIndex = i
    if myList[i] > max:
        max = myList[i]
        maxIndex = i
myList[minIndex], myList[maxIndex] = myList[maxIndex], myList[minIndex]
print(*myList, end='')
