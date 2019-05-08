inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')


class Student:
    Name = []
    exam_1 = 0
    exam_2 = 0
    exam_3 = 0
    total_score = 0


K = 0
passingScore = 0
peopleList = []
A = []
lines = inFile.readlines()
K = int(lines[0])
for line in lines:
    peopleList.append(list(line.split()))
del peopleList[0]
for i in peopleList:
    stud = Student()
    stud.Name = i[0:-3]
    stud.exam_1 = int(i[-3])
    stud.exam_2 = int(i[-2])
    stud.exam_3 = int(i[-1])
    stud.total_score = stud.exam_1 + stud.exam_2 + stud.exam_3
    if stud.exam_1 >= 40 and stud.exam_2 >= 40 and stud.exam_3 >= 40:
        A.append(stud)
A.sort(key=lambda stud: -stud.total_score)
if K >= len(A):
    passingScore = 0
elif A[0].total_score == A[K].total_score:
    passingScore = 1
elif K < len(A) and A[0].total_score != A[K-1].total_score and \
     A[K-1].total_score == A[K].total_score:
    while A[K].total_score == A[K - 1].total_score:
        K -= 1
    passingScore = A[K-1].total_score
else:
    passingScore = A[K-1].total_score
print(passingScore, end='', file=outFile)
inFile.close()
outFile.close()
