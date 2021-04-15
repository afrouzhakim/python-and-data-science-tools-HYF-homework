weight = float(input("Please input your weight in kilogram: "))
height = float(input("Please input your height in meter: "))

print("Your body mass index is: ", round(weight / (height * height), 2))
