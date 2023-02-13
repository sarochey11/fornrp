class Person:
    def __init__(self,n,g,h,w):
        self.name = n
        self.gender = g
        self.weight = h
        self.height = w
    def bmi(self, bmiStatus, weight, height, statusValue):
        bmiStatus = round(weight / (height/100) ** 2, 2)


        if bmiStatus < 18.5:
            statusValue = "Underweight"
        elif bmiStatus >= 18.5 and bmiStatus < 25:
            statusValue = "Normal"
        elif bmiStatus >= 25 and bmiStatus < 30:
            statusValue = "Overweight"
        else:
            statusValue = "Obese"
        return bmiStatus, statusValue
        

P = Person('Sean', 'Male', 185, 80)

# broken