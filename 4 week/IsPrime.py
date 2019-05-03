from math import sqrt


def IsPrime(n):
    i = 2
    while sqrt(n) >= i:
        if n % i == 0:
            return 'NO'
        i += 1
    return 'YES'
n = int(input())
print(IsPrime(n), end='')
