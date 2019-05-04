n = int(input())
for i in range(1, n + 1):
    if i != n:
        print('+___ ', end='')
    else:
        print('+___ ')
for i in range(1, n + 1):
    if i != n:
        print('|', i, ' / ', sep='', end='')
    else:
        print('|', i, ' / ', sep='')
for i in range(1, n + 1):
    if i != n:
        print("|__\ ", end='')
    else:
        print("|__\ ")
for i in range(1, n + 1):
        print('|    ', end='')
