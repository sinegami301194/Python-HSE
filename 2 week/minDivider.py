N = int(input())
i = 2
while i <= N:
    if N % i == 0:
        break
    i = i + 1
print(i, end=' ')
