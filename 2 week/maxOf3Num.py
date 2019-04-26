A = int(input())
B = int(input())
C = int(input())
if A > B:
    if A > C:
        print(A, end='')
    else:
        print(C, end='')
else:
    if B > C:
        print(B, end='')
    else:
        print(C, end='')
