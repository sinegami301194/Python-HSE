def IsPointInCircle(x, y, xc, yc, r):
    if (x - xc)**2 + (y - yc)**2 <= r**2:
        return True
    return False
x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES', end='')
else:
    print('No', end='')
