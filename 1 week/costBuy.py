A = int(input())
B = int(input())
N = int(input())
cost = (A*100 + B) * N
rub = cost // 100
kop = cost % 100
print(rub, kop, end='')
