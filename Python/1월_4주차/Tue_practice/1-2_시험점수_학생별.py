students = [
 [100, 80, 100],
 [90, 90, 60],
 [80, 80, 80]
]

for student in students:
    total = 0
    for subject in student:
        total += subject
    print(total)
