x = int(input())
sum = 0
while x != 0:
    if x % 2 == 0:
        sum = sum + 1
    x = int(input())
print(sum, end='')
