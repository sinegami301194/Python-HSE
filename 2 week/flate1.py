x = int(input())
y = int(input())
if y % (y - x + 1) == 0:
    print('YES', end='')
else:
    print('NO', end='')
