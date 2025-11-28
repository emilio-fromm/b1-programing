expense_records = []

category_totals = {}

unique_categories = set()


def getExpenses():
    amount = 0
    date = ""
    choosed = ""
    i = 0
    while i < 3:
        print("1. Please add a new category...")
        
        choosed = input()
        unique_categories.add(choosed)
        
        print("1. Please add the amount of the expense...")
        amount = input()
        try:
            amount = int(amount)
           
            
        except ValueError:
            print("input is not a number. Programm will restart now")
            getExpenses()
            break;
            
        print("Please input the date where the expense was issued... (Format: DD.MM.YY)")
        date = input()
        expense_records.append((choosed, amount, date))
        i = i + 1
                
            
      
            
               
                
    print(expense_records)


def addCategories():
    
    for tupel in expense_records:
            if tupel[0] not in unique_categories:
                unique_categories.add(tupel[0])
            
    print(unique_categories)
    

def calculateSpending():
    for tupel in expense_records:
        if tupel[0] not in category_totals.keys():
            print(tupel[0])
            print(tupel[1])
            category_totals.update({tupel[0] : tupel[1]})
        else:
            category_totals[tupel[0]] = category_totals[tupel[0]] + tupel[1]
    return category_totals

getExpenses()
addCategories()
calculateSpending()

def total_spending(calculateSpending):
    list = calculateSpending.values()
    totalSpending = 0
    for expense in list:
        totalSpending = totalSpending + expense
    
    print("Total Spending: " + str(totalSpending))
    return totalSpending


def highest_expense(calculateSpending):
    list = calculateSpending.items()
    highestTupel = ("", 0)
    highestExpense = -1
    for expense in list:
        
        if expense[1] > highestExpense:
            highestExpense = expense[1]
            highestTupel = expense
    
    print("Highest Expense: " + str(highestTupel))

def lowest_expense(calculateSpending):
    list = calculateSpending.items()
    lowestTupel = ("", 0)
    lowestExpense = -1
    for expense in list:
        if lowestExpense == -1:
            lowestTupel = expense
            lowestExpense = expense[1]
        else:
            if expense[1] < lowestExpense:
                lowestExpense = expense[1]
                lowestTupel = expense
    
    print("lowest Expense: " + str(lowestTupel))

def avg_expense(calculateSpending, totalSpending):
    print("AVG EXPENSE AMOUNT: " + str(totalSpending / int(len(calculateSpending))))
    return totalSpending / len(calculateSpending)





def overall_stats():
    print("Overall Stats: ")
    
    calculateSpending()
    total = total_spending(category_totals)
    highest_expense(category_totals)
    lowest_expense(category_totals)
    avg_expense(category_totals, total)

overall_stats()


