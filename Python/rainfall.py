

Columns = "{:<15} {:>2}".format

months_of_year  = {"Jan": "January","Feb": "February","Mar": "March"
                      ,"Apr": "April","May": "May","Jun": "June",
                   "Jul": "July","Aug": "August","Sep": "September",
                   "Oct": "October","Nov": "November","Dec": "December"}
amount_of_rain = [81,55,61,58,59,70,75,85,90,105,85,90]

rain_and_month = {"january": amount_of_rain[0], "february": amount_of_rain[1], "march": amount_of_rain[2], "april": amount_of_rain[3], "may": amount_of_rain[4], "june": amount_of_rain[5], "july": amount_of_rain[6], "august": amount_of_rain[7], "september": amount_of_rain[8], "october": amount_of_rain[9], "november": amount_of_rain[10], "december": amount_of_rain[11]}
min_value = min(amount_of_rain)
max_value = max(amount_of_rain)

def rainfall():
    print()
    print('Chorley Rainfall 2021')
    print(Columns("Month", "Total Rainfall"))
    for month, amount in zip(months_of_year, amount_of_rain):
        print(Columns(month, amount)) # Prints the months and the amount of rain
    
    
    average = sum(amount_of_rain) / len(amount_of_rain) # devide the total amount of rain by the amount of months
    print(Columns("\nAverage: ", round(average, 2))) # Creates a new line and prints the average and rounds it to 2 decimal places
    #print(Columns("Average:", sum(amount_of_rain) / len(amount_of_rain)))
    print(Columns("Minimum:", min(amount_of_rain)))
    print(Columns("Maximum:", max(amount_of_rain)))
    print(Columns("Total:", sum(amount_of_rain)))
    print()
    print(f"The lowest amount of rainfall was in " + str(months_of_year.get("Jan")) + ": " + str(min_value) + "mm")
    print(f"The highest amount of rainfall was in " + str(months_of_year.get("Dec")) + ": " + str(max_value) + "mm")



def choice():
    b = input("\nWhich month would you like to see the rain fall for, for all please type 'all'? ").lower()

    key_list = list(rain_and_month.keys()) # creates a list of the keys in from the dictionary
    val_list = list(rain_and_month.values()) # creates a list of the values in from the dictionary

    while b in rain_and_month:
        #print(val_list[key_list.index(b)], "mm")
        capsVal = b.capitalize()
        print(f"The amount of rainfall in " + capsVal + " was " + str(val_list[key_list.index(b)]) + "mm")
        choice()
    
    else:
        if b == "all":
            rainfall() 
            choice()
        else:
            print("Invalid input")
            choice()

print("Hello, \nThis program will show you the rainfall for the year 2021 in Chorley")
choice()