x1 = int(input()) # Input the number
y1 = int(input()) # Input the number
x2 = int(input()) # Input the number
y2 = int(input()) # Input the number
if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print('YES', end='')
else:
    print('NO', end='')
