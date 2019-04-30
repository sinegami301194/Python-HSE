s = input()
pos = s.find(' ', 0)
print(s[pos + 1:], s[:pos], end='')
