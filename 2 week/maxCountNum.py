big = 0
n = 0
x = int(input())
while x != 0:
    if x > big:
        big = x
        n = 0
    if x == big:
        n += 1
    x = int(input())
print(n, end='')
