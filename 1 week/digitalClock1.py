N = int(input()) # Input the integer
minutes = N % 60
H1 = N // 60
hours = H1 % 24
print(hours, minutes, end='')
