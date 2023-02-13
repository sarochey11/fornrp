i = 1
while i<=10:
    print ('student', i)
    exam1 = int(input("Enter 1st exam"))
    exam2 = int(input("Enter 2nd exam"))
    exam3 = int(input("Enter 3rd exam"))
    exam4 = int(input("Enter 4th exam"))
    exam5 = int(input("Enter 5th exam"))

    average = (exam1 + exam2 + exam3 + exam4 + exam5)/5

    if average >= 90:
        print('The average equals = {}, {}'.format(average, 'A'))
    elif average < 90 and average >= 80:
        print('The average equals = {}, {}'.format(average, 'B'))
    elif average < 80 and average >= 70:
        print('The average equals = {}, {}'.format(average, 'C'))
    elif average < 70 and average >=60:
        print('The average equals = {}, {}'.format(average, 'D'))
    elif average < 60 and average >= 50:
        print('The average equals = {}, {}'.format(average, 'E'))
    else:
        print('The average equals = {}, {}'.format(average, 'F'))
    i += 1