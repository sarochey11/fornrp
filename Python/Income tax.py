income =float(input("Enter the annual income: ")) # Get the income

if income < 85528: # Get the monthly income
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32 

if tax < 0: # If the tax is negative, set it to 0
    tax = 0


tax = round(tax, 0) # Round the tax to the nearest whole number
print ("Your tax is:", tax, "thalers") # Print the tax amount