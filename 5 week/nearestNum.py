N = int(input())
myList = list(map(int, input().split()))
x = int(input())
min = 2001
index = 0
for i in range(0, N):
    if abs(x - myList[i]) < min:
        min = abs(x - myList[i])
        index = i
print(myList[index], end='')
