# Copyright by Emilio

student_records = []

print("=== GRADE ANALYSIS ===\n")
print("testig input system...")

for i in range(1, 7):
    name = input(f"Student {i} name: ")
    score = int(input(f"Student {i} score: "))
    student_records.append((name, score))
    print()

scores = []
for name, score in student_records:
    scores.append(score)

highest = max(scores)
lowest = min(scores)
average = sum(scores) / len(scores)

unique_scores = set(scores)

grade_distribution = {}
for score in scores:
    grade_distribution[score] = grade_distribution.get(score, 0) + 1

print("\n=== STUDENT OVERVIEW ===")
for i, (name, score) in enumerate(student_records, 1):
    if score >= 90:
        letter = "A"
    elif score >= 80:
        letter = "B"
    elif score >= 70:
        letter = "C"
    elif score >= 60:
        letter = "D"
    else:
        letter = "F"
    print(f"{i}. {name}: {score} points ({letter})")

print("\n=== CLASS STATISTICS ===")
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")
print(f"Average: {average:.2f}")

print("\n=== UNIQUE SCORES ===")
print(unique_scores)
print(f"Number of unique scores: {len(unique_scores)}")

print("\n=== SCORE DISTRIBUTION ===")
for score in sorted(grade_distribution.keys(), reverse=True):
    count = grade_distribution[score]
    label = "student(s)"
    print(f"Score {score}: {count} {label}")

passed_list = [(n, s) for n, s in student_records if s >= 60]
failed_list = [(n, s) for n, s in student_records if s < 60]
print(f"\nPassed: {len(passed_list)} | Failed: {len(failed_list)}")

top = max(student_records, key=lambda x: x[1])
bottom = min(student_records, key=lambda x: x[1])
print(f"Top student: {top[0]} ({top[1]} points)")
print(f"Needs help: {bottom[0]} ({bottom[1]} points)")
