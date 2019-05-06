N = int(input())
A = list(map(int, input().split()))
B = sorted(A)
print(*B, end='')
