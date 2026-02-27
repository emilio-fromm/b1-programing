# Copyright by Emilio

import string
import random

secList = ["!", "§", "$", "%", "&", "/", "(", ")", "=", "`", "?"]
previously_used = ["Password1!", "Summer2023!", "Test1234!"]


def check_min_length(password, min_len=8):
    if len(password) >= min_len:
        return True
    return False

def has_uppercase(password):
    for letter in password:
        if letter.isupper():
            return True
    return False


def has_lowercase(password):
    for letter in password:
        if letter.islower():
            return True
    return False

def has_digit(password):
    for letter in password:
        if letter.isdigit():
            return True
    return False


def has_special_char(password):
    for letter in password:
        if letter in string.punctuation:
            return True
    return False


def check_previously_used(password):
    if password in previously_used:
        return True
    return False

def get_strength_score(password):
    score = 0
    if check_min_length(password):
        score = score + 1
    if has_uppercase(password):
        score = score + 1
    if has_lowercase(password):
        score = score + 1
    if has_digit(password):
        score = score + 1
    if has_special_char(password):
        score = score + 1
    return score


def pass_gen(password):
    return password + random.choice(secList)


def password_checker(password):
    print("deubg - passwort wird gecheckt")
    isWeak = False

    if check_previously_used(password):
        print("WARNING: This password was used before!")
        isWeak = True

    if check_min_length(password):
        print("Length test: passed")
    else:
        print("Length test: failed")
        isWeak = True

    if has_uppercase(password):
        print("Uppercase test: passed")
    else:
        print("Uppercase test: failed")
        isWeak = True

    if has_lowercase(password):
        print("Lowercase test: passed")
    else:
        print("Lowercase test: failed")
        isWeak = True

    if has_digit(password):
        print("Digit test: passed")
    else:
        print("Digit test: failed")
        isWeak = True

    if has_special_char(password):
        print("Special Char test: passed")
    else:
        print("Special Char test: failed")
        isWeak = True

    score = get_strength_score(password)
    print(f"\nStrength score: {score}/5")

    if isWeak:
        print("Your password is weak")
        q = input("Do you want to make it stronger? (y/n): ")
        if q == "y" or q == "Y":
            new_pw = pass_gen(password)
            print("Your new password is:", new_pw)
            previously_used.append(password)
    else:
        print("Your password is strong!")
        previously_used.append(password)


password = input("Enter a password to check: ")
password_checker(password)
