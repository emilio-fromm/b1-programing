
passwords = [ "Pass123",
"SecurePassword1", "weak",
"MyP@ssw0rd", "NOLOWER123"]

lc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

numbers = [0,1,2,3,4,5,6,7,8,9]

lFound = False
uFound = False
number = False
for password in passwords:
    print("zu überprüfendes Passwort.... ",password)
    if len(password) < 9:
        print("Your password needs at least 8 characters")
        
    for letter in lc:
        for letter2 in password:
            if letter == letter2:
                lFound = True
    
    if lFound == False:
        print("Bitte füge einen Kleinbuchstaben ein")
    
    for letter in uc:
        for letter2 in password:
            if letter == letter2:
                uFound = True
    
    if uFound == False:
        print("Bitte füge einen Großbuchstaben ein")
    
    
        
    for number in numbers:
        for letter2 in password:
            if  number == letter2:
                number = True
    
    if lFound == False:
        print("Bitte füge eine Zahl ein")

    lFound = False
    uFound = False
    number = False
    
