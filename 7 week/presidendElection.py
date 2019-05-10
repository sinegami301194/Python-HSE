import io

candidates = {}
voices = 0

with io.open("input.txt", "r", encoding="utf-8") as inFile:
    for name in map(str.strip, inFile):
        candidates[name] = candidates.get(name, 0) + 1
        voices += 1


candidates = sorted(candidates.items(), key=lambda x: x[1], reverse=True)

with io.open("output.txt", "w", encoding="utf-8") as outFile:
    percent = candidates[0][1] / voices * 100
    if percent > 50:
        print(candidates[0][0], file=outFile)
    else:
        for name, _ in candidates[:2]:
            print(name, file=outFile)
inFile.close()
outFile.close()
