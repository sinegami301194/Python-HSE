x = int(input())
max = x
while x != 0:
    if x > max:
        max = x
    x = int(input())
print(max, end='')
