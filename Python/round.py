Columns = "{:<15} {:>2}".format

months_of_year = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"}

amound_of_rain = [81, 55, 61, 58, 59, 70, 75, 85, 90, 105, 85, 90]

min_value = min(amound_of_rain)
max_value = max(amound_of_rain)

def rainfall():
    print()
    print("Chorley Rainfall 2021")
    print(Columns("Month", "Rainfall"))
    for month, amount in zip(months_of_year, amound_of_rain):
        print(Columns(month, amount))
    
    print(Columns("Average", sum(amound_of_rain) / len(amound_of_rain)))
    print(Columns("Minimum", min_value(amound_of_rain)))
    print(Columns("Maximum", max_value(amound_of_rain)))
    print(Columns("Total", sum(amound_of_rain)))
    print()