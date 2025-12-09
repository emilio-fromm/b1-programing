import os

temp = []
def saveFile():
    try:
        with open("products.txt") as file:
            for line in file:
                line = line.strip()
                lineFormatted = line.split(",")
                temp.append(lineFormatted)
    except FileNotFoundError:
        print("The file was not found by the system!")
    except PermissionError:
        print("Can not open the file because of insufficient permission!")
    

def getCatDiscount(category):
    match category:
        case "Electronics":
            return 0.1
        case "Clothing":
            return 0.2
        case "Books":
            return 0.25
        case "Home":
            return 0.05
    
    return 0
    
    
   
def getTierDiscount(tier):
    if tier == "Premium":
        return 0.1
    else:
        return 0.2
    
def discountProducts(productList):
    list = []
    for element in productList:
        
        print(element[1])
        try:
            discount =  (getCatDiscount(element[2]) + getTierDiscount(element[3]))*100
            print("discount: ",  discount, "%")
            discountedPrice = float(element[1]) * float((100-discount) * 0.01)
            print("discounted Price: ", discountedPrice)
        
            list.append([element[0], element[1], discount, discountedPrice])
        except ValueError:
            print("Some of the provided data is in wrong format, please check!")
            
    return list
    
    
def createFile(list):
    try:
        with open("pricing_report.txt", "x") as f:
            f.write("Discounted Product Price List: \n\n")
            for element in list:
                f.write("Product Name: " + str(element[0]) + "\n")
                f.write("Original Price: " + str(element[1]) + "\n")
                f.write("Discount: " + str(element[2]) + "%" + "\n")
                f.write("Discounted Price " + str(element[3]) + "\n\n")
                
    except FileExistsError:
            print("Delete existing file...")
            os.remove("pricing_report.txt")
            print(f"File 'pricing_report.txt' successfully deleted! -  Creating new one...")
            createFile(list)
    except PermissionError:
        print("Can not open the file because of insufficient permission!")
    
        
            
      
        
saveFile()
createFile(discountProducts(temp))
print(temp)






