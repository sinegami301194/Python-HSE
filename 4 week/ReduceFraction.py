def ReduceFraction(n, m):
    def gdB(a, b):
        while a % b:
            a, b = b, a % b
        return int(b)
    g = gdB(n, m)
    return int(n / g), int(m / g)
n = int(input())
m = int(input())
print(*ReduceFraction(n, m), end='')
