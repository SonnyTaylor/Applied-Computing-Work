classroom_roster = [
    ["Alice", [85, 90, 78]],
    ["Bob", [90, 80, 89]],
    ["Charlie", [70, 75, 72]],
    ["David", [60, 65, 62]],
]

print("Classroom Roster")
for student in classroom_roster:
    name = student[0]
    grades = student[1]
    print(f"Name: {name}, Grades: {grades}")
