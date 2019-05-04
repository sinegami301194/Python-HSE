def deg():
    n = int(input())
    if n == 0:
        return 0
    return n + deg()
print(deg(), end='')
