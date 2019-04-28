x = int(input())
sum = 0
i = 0
while x != 0:
    sum = sum + x
    i = i + 1
    x = int(input())
print(sum / i, end='')
