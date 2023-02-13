import datetime

date = input('Please enter date DD/MM/YYYY: ') # Input date
d1 = datetime.datetime.strptime(date, '%d/%m/%Y').date() # Convert date to datetime format
d2 = datetime.datetime.strptime('15/10/2022', '%d/%m/%Y').date() # Required datein datetime format
age = int(input('Please enter your age: ')) # Input age
risk = input('clinical rish group (true/false): ') # Input risk


if age >= 18 and age <= 64 and risk == "true": # Check if age is between 18 and 64 and risk is true
    print('You are eligible for a free flu jab') 
elif age >= 50 and age <= 64 and risk == "false" and d1 > d2: # Check if age is between 50 and 64 and risk is false and date is after 15/10/2022
    print('You are eligible for a free flu jab')
elif age > 65: # Check if age is greater than 65
    print('You are eligible for a free flu jab')
else:
    print('You can get a Flu Jab for £15.99')