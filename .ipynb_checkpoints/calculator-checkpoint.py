""" A  functional calculator that accepts user input, performs calculations, and displays formatted results with proper error handling and documentation """

# Here the revenue and costs are taken from the user (Input) 
revenue = input("your revenue")
cost = input("your costs")

# profit is calculated with a simple substractioon + it is converted to percentage
    
profit = ((int(revenue)) - (int(cost)) ) * 100



#Output
print("The profit of your company is: ", profit, "€")
print(f"Why? -> Your Revenue was: {revenue} and your Costs were: {cost}")   
        



