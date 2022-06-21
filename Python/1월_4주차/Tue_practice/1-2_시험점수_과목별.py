students = [
 [100, 80, 100],
 [90, 90, 60],
 [80, 80, 80]
]

for i in range(len(students[0])):
    total = 0
    for j in range(len(students)):
        total += students[j][i]
    print(total)