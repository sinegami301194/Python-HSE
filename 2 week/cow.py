n = int(input())
if n % 10 == 1 and n // 10 != 1:
    print(n, 'korova', end='')
else:
    if n % 10 > 1 and n % 10 < 5 and n // 10 != 1:
        print(n, 'korovy', end='')
    else:
        if n % 10 > 4 or n % 10 == 0 or n // 10 == 1:
            print(n, 'korov', end='')
