# Copyright by Emilio

expense_records = []
category_totals = {}
unique_categories = set()

MONTHLY_BUDGET = 500.0

print("=== EMILIO'S EXPENSE TRACKER ===\n")
print("Logging expenses...")

for i in range(1, 6):
    category = input(f"Expense {i} category: ")
    amount = input(f"Expense {i} amount: ")
    date = input(f"Expense {i} date (YYYY-MM-DD): ")
    print()

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid input, setting amount to 0")
        amount = 0.0

    expense_records.append((category, amount, date))
    unique_categories.add(category)
    category_totals[category] = category_totals.get(category, 0) + amount

all_amounts = []
for cat, amt, dt in expense_records:
    all_amounts.append(amt)

total = sum(all_amounts)
average = total / len(all_amounts)

highest_record = expense_records[0]
lowest_record = expense_records[0]
for record in expense_records:
    if record[1] > highest_record[1]:
        highest_record = record
    if record[1] < lowest_record[1]:
        lowest_record = record

print("deubg - calucating stats now")

print("=== EXPENSE SUMMARY ===")
print(f"Total spending: {total:.2f} Euro")
print(f"Average: {average:.2f} Euro")
print(f"Highest expense: {highest_record[1]:.2f} Euro (category: {highest_record[0]}, date: {highest_record[2]})")
print(f"Lowest expense: {lowest_record[1]:.2f} Euro (category: {lowest_record[0]}, date: {lowest_record[2]})")

if total > MONTHLY_BUDGET:
    over = total - MONTHLY_BUDGET
    print(f"\nWARNING: You exceeded your monthly budget by {over:.2f} Euro!")
else:
    remaining = MONTHLY_BUDGET - total
    print(f"\nBudget OK! {remaining:.2f} Euro remaining from monthly budget")

print("\n=== CATEGORIES ===")
print(unique_categories)
print(f"Number of unique categories: {len(unique_categories)}")

print("\n=== SPENDING BY CATEGORY ===")
for category, total_cat in category_totals.items():
    percent = (total_cat / total) * 100 if total > 0 else 0
    print(f"{category}: {total_cat:.2f} Euro ({percent:.1f}%)")
