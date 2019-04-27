A, B, C = int(input()), int(input()), int(input())
D, E, F = int(input()), int(input()), int(input())
if A == D and (B == E and C == F or B == F and C == E):
    print('Boxes are equal', end='')
elif B == D and (A == E and C == F or A == F and C == E):
    print('Boxes are equal', end='')
elif C == D and (B == E and A == F or B == F and A == E):
    print('Boxes are equal', end='')
elif A <= D and (B <= E and C <= F or B <= F and C <= E):
    print('The first box is smaller than the second one', end='')
elif B <= D and (A <= E and C <= F or A <= F and C <= E):
    print('The first box is smaller than the second one', end='')
elif C <= D and (B <= E and A <= F or B <= F and A <= E):
    print('The first box is smaller than the second one', end='')
elif A >= D and (B >= E and C >= F or B >= F and C >= E):
    print('The first box is larger than the second one', end='')
elif B >= D and (A >= E and C >= F or A >= F and C >= E):
    print('The first box is larger than the second one', end='')
elif C >= D and (B >= E and A >= F or B >= F and A >= E):
    print('The first box is larger than the second one', end='')
else:
    print('Boxes are incomparable', end='')
