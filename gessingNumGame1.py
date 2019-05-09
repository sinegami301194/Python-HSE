with open("input.txt", "r", encoding="utf8") as in_file:
    x = int(in_file.readline())
    answer = set(range(1, x + 1))
    temp = set()
    for line in in_file:
        if "YES" in line:
            answer &= temp
        elif "NO" in line:
            answer -= temp
        elif "HELP" not in line:
            temp = set(map(int, line.split()))
print(' '.join(map(str, sorted(answer))))
