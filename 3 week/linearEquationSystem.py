a, b, c = float(input()), float(input()), float(input()) # Creating the float numbers
d, e, f = float(input()), float(input()), float(input()) # Creating the float numbers
if b != 0:
    y = (c * e - a * f) / (b * c - a * d)
    if c != 0:
        x = (f - d * y) / c
        print(x, y, end='')
else:
    if a != 0:
        x = (f * b - d * e) / (b * c - d * a)
        if d != 0:
            y = (f - c * x) / d
            print(x, y, end='')
