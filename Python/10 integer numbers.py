userInteger = []

for i in range(10):
    userInteger.append(int(input('Enter integer ' + str(i+1) + ' :')))
    print("You entered: ", userInteger)
    for i in range(len(userInteger)-1):
        print("*", end = "")


''' 
print('Enter 10 intgers')
histogram_val =[]
for i in range(10):
    histogram_val.append(int(input('Enter integer ' + str(i+1) + ' :')))
print (histogram_val) 
'''

#print the histogram