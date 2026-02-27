# Copyright by Emilio

print("=== Simple Calculator ===")
print("Los geht's!")

history = []

print("testig if input works...")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operation = input("Choose operation (+, -, *, /): ")

print("calucating...")

try:
    num1 = float(num1)
    num2 = float(num2)
    result = None

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed")
        else:
            result = num1 / num2
    else:
        print("Unknown operation. Please use +, -, * or /")

    if result is not None:
        print(f"Result: {num1} {operation} {num2} = {result}")
        history.append(f"{num1} {operation} {num2} = {result}")

except ValueError:
    print("Error: Please enter valid numbers")

more = input("\nDo another calculation? (y/n): ")
while more == "y" or more == "Y":
    print("loadign next calculation...")
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    operation = input("Choose operation (+, -, *, /): ")
    try:
        num1 = float(num1)
        num2 = float(num2)
        result = None
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero!")
            else:
                result = num1 / num2
        else:
            print("Unknown operation")
        if result is not None:
            print(f"Result: {num1} {operation} {num2} = {result}")
            history.append(f"{num1} {operation} {num2} = {result}")
    except ValueError:
        print("Error: Please enter valid numbers")
    more = input("\nDo another calculation? (y/n): ")

print("\n=== Calculation History ===")
if len(history) == 0:
    print("No calculations done")
else:
    for i, entry in enumerate(history, 1):
        print(f"{i}. {entry}")
print("Fertig!")
