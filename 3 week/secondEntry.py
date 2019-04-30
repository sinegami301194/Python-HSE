s = input()
if s.find('f', 0) == -1:
    print(-2, end='')
else:
    pos = s.find('f', 0)
    if s.find('f', pos + 1) != -1:
        print(s.find('f', pos + 1), end='')
    else:
        print(-1, end='')
