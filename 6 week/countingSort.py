def CountSort(A):
    B = []
    for i in range(n):
        B.append(min(A))
        A.remove(min(A))
    return B
myList = list(map(int, input().split()))
n = len(myList)
answer = CountSort(myList)
for j in range(n - 1):
    print(answer[j], end=' ')
print(answer[n - 1], end='')
