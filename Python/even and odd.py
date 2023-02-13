counter = int(input("Enter the number or type 0 to stop: "))
even = 0
odd = 0
while counter != 0:
    if (counter %2) == 0:
        even ++ 1
        print("The number is even")
        counter = int(input("Enter the number or type 0 to stop: "))
    
    else:
        odd ++ 1
        print("The number is odd")
        counter = int(input("Enter the number or type 0 to stop: "))
print("The number 0 entered. The program will stop now.")