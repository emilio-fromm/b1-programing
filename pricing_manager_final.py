# Copyright by Emilio

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
        print("File not found!")
    except PermissionError:
        print("No permission to open the file!")



def getCatDiscount(category):
    if category == "Electronics":
        return 0.10
    elif category == "Clothing":
        return 0.15
    elif category == "Books":
        return 0.05
    elif category == "Home":
        return 0.12
    return 0


def getTierDiscount(tier):
    if tier == "Premium":
        return 0.05
    elif tier == "Budget":
        return 0.02
    return 0

def discountProducts(productList):
    print("deubg - calucating discounts")
    result = []
    for element in productList:
        try:
            discount = (getCatDiscount(element[2]) + getTierDiscount(element[3])) * 100
            discountedPrice = float(element[1]) * ((100 - discount) * 0.01)
            savings = float(element[1]) - discountedPrice
            result.append([element[0], element[1], discount, discountedPrice, savings])
        except ValueError:
            print("Bad data, please check!")
    return result


def getBestDeal(discountedList):
    if not discountedList:
        return None
    best = discountedList[0]
    for item in discountedList:
        if item[4] > best[4]:
            best = item
    return best



def createFile(list):
    totalDiscount = 0
    totalSavings = 0
    try:
        with open("pricing_report.txt", "x") as f:
            f.write("Discounted Product List: \n\n")
            for element in list:
                totalDiscount = totalDiscount + element[2]
                totalSavings = totalSavings + element[4]
                f.write("Product name: " + str(element[0]) + "\n")
                f.write("Original price: " + str(element[1]) + "\n")
                f.write("Discount: " + str(element[2]) + "%" + "\n")
                f.write("Discounted price: " + str(round(element[3], 2)) + "\n")
                f.write("Savings: " + str(round(element[4], 2)) + "\n\n")

            print("Average discount: ", round(totalDiscount / len(list), 2), "%")
            print("Total savings: $" + str(round(totalSavings, 2)))

    except FileExistsError:
        print("Deleting old file...")
        os.remove("pricing_report.txt")
        print("File deleted! Creating new one...")
        createFile(list)
    except PermissionError:
        print("No permission!")

    print("Products processed: ", len(list))

    best = getBestDeal(list)
    if best:
        print(f"Best deal: {best[0]} saves ${round(best[4], 2)}")


saveFile()
print("loadign products done, staring discount calucations...")
createFile(discountProducts(temp))
