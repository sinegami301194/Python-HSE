A = int(input()) # Creating number
if A % 400 == 0:
    print('YES', end='')
else:
    if A % 100 == 0:
        print('NO', end='')
    else:
        if A % 4 == 0:
            print('YES', end='')
        else:
            print('NO', end='')
