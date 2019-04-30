import math
n = float(input())
x = int((n * 10) % 10)
if x >= 5:
    print(math.ceil(n))
else:
    print(math.floor(n))
