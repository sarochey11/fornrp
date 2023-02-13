differentProducts = [1, 2, 3, 4, 5]
salesPeople = int(input("Enter the number of Sales People: "))
dailySales = []
total = ""

def create_dictionary(salesPeople):
    for i in range(salesPeople):
        dailySales.append({})


while salesPeople != 0:
    sales = 0
    for i in range(salesPeople):
        currPerson = i + 1
        print(f"Enter the number of units sold by Sales Person {currPerson}\n")
        for j in differentProducts:
            units = int(input(f"Product {j}: "))
            sales += units
            dailySales.append(sales)
            for i in dailySales:
                total = (f"Sales Person: {currPerson}, Number of sales: {sales}$")
        print(total)
    print("\n----------------------------------------")
    salesPeople = int(input("Enter the number of Sales People: "))