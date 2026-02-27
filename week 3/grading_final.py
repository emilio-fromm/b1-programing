# Copyright by Emilio

student_records = []

print("Enter grades for 3 students:")
print("testig input loop...")

for i in range(3):
    name = input("Student name: ")

    try:
        score = int(input("Score (0-100): "))
    except ValueError:
        print("Invalid input, setting score to 0")
        score = 0

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    student_records.append([name, score, grade])

print("\n=== Results ===")
for record in student_records:
    print(f"{record[0]}: {record[1]} points -> Grade {record[2]}")

scores = []
for record in student_records:
    scores.append(record[1])

print(f"\nHighest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")
print(f"Average score: {sum(scores) / len(scores):.1f}")

print("\n=== GRADE DISTRIBUTION ===")
grade_dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
for record in student_records:
    grade_dist[record[2]] = grade_dist[record[2]] + 1

for grade, count in grade_dist.items():
    if count > 0:
        print(f"Grade {grade}: {count} student(s)")

passed = 0
for record in student_records:
    if record[1] >= 60:
        passed = passed + 1
failed_students = len(student_records) - passed
print(f"\nPassed: {passed} | Failed: {failed_students}")

top_student = student_records[0]
for record in student_records:
    if record[1] > top_student[1]:
        top_student = record
print(f"Top student: {top_student[0]} with {top_student[1]} points")
print("Fertig!")
