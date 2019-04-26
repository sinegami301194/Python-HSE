a, b, c = int(input()), int(input()), int(input())
if a == b and a == c:
    print(3, end='')
if a == b and a != c or a != b and a == c or b == c and c != a:
    print(2, end='')
if a != b and a != c and b != c:
    print(0, end='')
