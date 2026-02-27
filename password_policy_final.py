# Copyright by Emilio

import string
import random


def check_min_length(password, min_len=8):
    return len(password) >= min_len


def has_uppercase(password):
    return any(char in string.ascii_uppercase for char in password)

def has_lowercase(password):
    return any(char in string.ascii_lowercase for char in password)


def has_digit(password):
    return any(char in string.digits for char in password)

def has_special_char(password):
    return any(char in string.punctuation for char in password)


def validate_password(password):
    print("deubg - wird validiert")
    results = {
        "min_length": check_min_length(password),
        "has_uppercase": has_uppercase(password),
        "has_lowercase": has_lowercase(password),
        "has_digit": has_digit(password),
        "has_special": has_special_char(password)
    }
    results["is_valid"] = all(results.values())
    return results


def get_strength_meter(results):
    passed = sum(1 for k, v in results.items() if k != "is_valid" and v)
    bar = "#" * passed + "-" * (5 - passed)
    return f"[{bar}] {passed}/5"

def generate_strong_password(length=12):
    print("genrating passwrod...")
    chars = string.ascii_letters + string.digits + "!@#$%&"
    while True:
        pw = "".join(random.choice(chars) for _ in range(length))
        res = validate_password(pw)
        if res["is_valid"]:
            return pw


password = input("Enter a password to validate: ")
results = validate_password(password)

print("\n--- Validation Results ---")
print("Min length (8+):   ", "OK" if results["min_length"] else "FAIL")
print("Uppercase letter:  ", "OK" if results["has_uppercase"] else "FAIL")
print("Lowercase letter:  ", "OK" if results["has_lowercase"] else "FAIL")
print("Contains digit:    ", "OK" if results["has_digit"] else "FAIL")
print("Special character: ", "OK" if results["has_special"] else "FAIL")

print("\nStrength meter:", get_strength_meter(results))

if results["is_valid"]:
    print("\nYour password is STRONG!")
else:
    print("\nYour password is WEAK!")
    hints = [
        "Try adding a number like 42",
        "Use a mix of uppercase and lowercase letters",
        "Add a special character like ! or @",
        "Make it at least 8 characters long"
    ]
    print("Tip:", random.choice(hints))
    suggest = input("Generate a strong password for you? (y/n): ")
    if suggest == "y" or suggest == "Y":
        new_pw = generate_strong_password()
        print("Suggested password:", new_pw)
