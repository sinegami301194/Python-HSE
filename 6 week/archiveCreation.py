C = list(map(int, input().split()))
A = []
sum = 0
count = 0
for i in range(0, C[1]):
    A.insert(i, int(input()))
B = sorted(A)
for j in range(0, len(B)):
    sum += B[j]
    if C[0] >= sum:
        count += 1
print(count, end='')
