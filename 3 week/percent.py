import math
a, b, c = float(input()), float(input()), float(input())
eps = 10**(-6)
D = b**2 - 4 * a * c
if D + eps > 0:
    x1 = (-b - math.sqrt(D)) / (2 * a)
    x2 = (-b + math.sqrt(D)) / (2 * a)
    if x1 % 1 == 0:
        x1 = round(x1)
    if x2 % 1 == 0:
        x2 = round(x2)
    if x1 > x2:
        print(x2, x1, end='')
    else:
        print(x1, x2, end='')
if D == 0:
    x = -b /(2 * a)
    if x % 1 == 0:
        x = round(x)
    print(x, end='')
