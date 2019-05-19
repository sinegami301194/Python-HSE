def IsPointInSquare(x, y): # Function declaration
    if x >= -1 and x <= 1 and y >= -1 and y <= 1:
        return True
    return False
x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES', end='')
else:
    print('No', end='')
