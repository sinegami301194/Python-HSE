def deg(a, n):
    if n == 1:
        return a
    if n != 0:
        if n % 2 == 0:
            return deg(a**2, n / 2)
        if n % 2 != 0:
            return a * deg(a, n - 1)
    return 1
a = float(input())
n = int(input())
print(deg(a, n), end='')
