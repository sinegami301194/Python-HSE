N = int(input()) # Input the integer
ss = N % 60
s1 = ss // 10
s2 = ss % 10
mm1 = N // 60
mm = mm1 % 60
m1 = mm // 10
m2 = mm % 10
hh1 = N // 3600
hh = hh1 % 24
print(hh, ':', m1, m2, ':', s1, s2, sep='') # Print value
