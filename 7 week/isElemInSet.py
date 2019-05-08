myList = list(map(int, input().split()))
mySet = set()
for elem in myList:
    if elem not in mySet:
        mySet.add(elem)
        print('NO')
    else:
        print('YES')
