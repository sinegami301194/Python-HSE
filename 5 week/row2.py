A = int(input())
B = int(input())
if A <= B:
    for i in range(A, B + 1):
        print(i, end=' ')
elif A > B:
    for i in range(A, B - 1, -1):
        print(i, end=' ')
