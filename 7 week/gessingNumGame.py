positiveSet = set()
negativeSet = set()
lines = []
line = True
while line:
    line = input().split()
    if line:
        lines.append(line)
N = int(lines[0][0])
for i in range(1, len(lines) - 1):
    if i % 2 == 0:
        if lines[i][0] == 'YES':
            positiveSet |= set(lines[i-1])
        else:
            negativeSet |= set(lines[i-1])
mySet = positiveSet - negativeSet
print(*mySet)
