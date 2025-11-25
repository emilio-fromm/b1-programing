import string
import random
passwords = ["hjgdfhjgsfd"]
secList = ["!","§","$","%","&","/","(",")","=","`","?"]

def check_min_length(password, min_len=8):
    if len(password) <= min_len:
           return False
           
    return False

def has_uppercase(password):
    for letter in password:
        if letter.isupper() == True:
            return True
    return False
    
    
    
def has_lowercase(password):
    for letter in password:
        if letter.islower() == True:
            return True
    return False
    
    
def has_digit(password):
    for letter in password:
        if letter.isdigit() == True:
            return True
    return False
    
def has_special_char(password):
    for letter in password:
        if letter in string.punctuation == True:
            return True
    return False

def pass_gen(password):
    password = password + random.choice(secList)
    
    return password
    

def password_checker(password):
    isWeak = False
    if check_min_length(password) == True:
        print("Length test: passed")
    else:
        print("length test: failed")
        isWeak = True
        
    if has_uppercase(password) == True:
        print("Uppercase test: passed")
    else:
        print("Uppercase test: failed")
        isWeak = True
        
    if has_lowercase(password) == True:
        print("Lowercase test: passed")
    else:
        print("Lowercase test: failed")
        isWeak = True
        
    if has_digit(password) == True:
        print("Digit test: passed")
    else:
        print("Digit test: failed")
        isWeak = True
    if has_special_char(password) == True:
        print("Special Char test: passed")
    else:
        print("Special Char test: failed")
        isWeak = True
        
    
    if isWeak == True:
        print("Your password is weak")
        print("")
        
        print("Do you want to make it Strong? // y / n")
        
        q = input()
        if q == "y" or "Y":
            print("Your new password is: ", pass_gen(password))
        else:
            print("Okay, good to know I´ll call my Indian Friends - see you at the ransomware payment")
    else:
        print("Your password is strong")
        
        
password_checker("Nm4dkjewfbui389)")
    


