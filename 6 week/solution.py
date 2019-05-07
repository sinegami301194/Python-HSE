readFromFile = open('input.txt', 'r', encoding='utf8')
writeInFile = open('output.txt', 'w', encoding='utf8')

#%%
class Student:
    Surname = ''
    Name = ''
    school = 0
    score = 0     

#%%
def sortStudent(A):
    for j in range(0, len(A) - 1):
        for i in range(0, len(A) - 1):
            if A[i].Surname < A[i+1].Surname:
                A[i],A[i + 1] = A[i + 1], A[i]
        A.sort
    return A
 
    
 #%%   
peopleList = []
A = []
#%%
lines = readFromFile.readlines()
for line in lines:
    peopleList.extend(list(line.split()))
#%%
for i in range(len(peopleList) // 4):
    stud = Student()
    stud.Surname = str(peopleList[4 * i])
    stud.Name = str(peopleList[4 * i + 1])
    stud.school = int(peopleList[4 * i + 2])
    stud.score = int(peopleList[4 * i + 3])
    A.append(stud)
#%%
   # print(A[line])
print(peopleList)
B = sortStudent(A)
for j in range(0, len(A) - 1):
    print(B[j].Surname, B[j].Name, B[j].score)
#A = list(peopleList.sort())
