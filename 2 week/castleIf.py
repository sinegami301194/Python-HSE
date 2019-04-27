A, B, C = int(input()), int(input()), int(input())
D, E = int(input()), int(input())
if A <= D and (B <= E or C <= E):
    print('YES', end='')
elif A <= E and (B <= D or C <= D):
    print('YES', end='')
elif B <= E and (A <= D or C <= D):
    print('YES', end='')
elif B <= D and (A <= E or C <= E):
    print('YES', end='')
elif C <= E and (A <= D or B <= D):
    print('YES', end='')
elif C <= D and (A <= E or B <= E):
    print('YES', end='')
else:
    print('NO', end='')
