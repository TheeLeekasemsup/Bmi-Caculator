print("Welcome to the Bmi caculator")

#input for weight
print("Please enter your weight in kg")
kg = int(input("")) 

#input for height
print("Please enter your height")
height = int(input("")) / 100

#print out weight and height 
print("your weight is:",kg)
print("your height is:",height)

#print our bmi
print("your Bmi is:",kg / (height * height))
