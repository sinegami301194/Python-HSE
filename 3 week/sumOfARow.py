a = int(input())
sum = 0
x = 1
while x <= a:
    sum += 1 / x**2
    x += 1
print(sum, end='')
