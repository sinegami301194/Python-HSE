myList = list(map(int, input().split()))
if len(myList) % 2 == 0:
    for i in range(0, len(myList) // 2):
        myList[2 * i], myList[2 * i + 1] = myList[2 * i + 1], myList[2 * i]
        i += 1
else:
    for i in range(0, (len(myList)) // 2):
        myList[2 * i], myList[2 * i + 1] = myList[2 * i + 1], myList[2 * i]
        i += 1
print(*myList, end='')
