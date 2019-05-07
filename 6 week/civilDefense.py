n = int(input())
A = map(int, input().split())
m = int(input())
B = list(map(int, input().split()))
for i in range(len(B)):
    B[i] = [i + 1, B[i]]
B.sort(key=lambda x: x[1])


def solve(x):
    if(x < B[0][1]):
        return B[0][0]
    if(x > B[-1][1]):
        return B[-1][0]
    l = 0
    r = len(B) - 1
    while(r - l > 1):
        m = (r + l) >> 1
        if(B[m][1] < x):
            l = m
        else:
            r = m
    if(x - B[l][1] < B[r][1] - x):
        return B[l][0]
    else:
        return B[r][0]
print(*[solve(s) for s in A])
