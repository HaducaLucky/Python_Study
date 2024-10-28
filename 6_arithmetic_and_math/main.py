
#! Ex. 2
# friends = 10

# # friends = friends + 1
# # friends += 1
# # friends = friends - 2
# # friends -= 2
# # friends = friends * 3
# # friends *= 3
# # friends = friends / 2
# # friends /= 2
# # friends = friends ** 2
# # friends **= 2
# # remainder = friends % 3

# print(remainder)

#! Ex. 2
# x = 3.14
# y = 4
# z = 5

# # result = round(x)
# # result = abs(y)
# # result = pow(4, 3)
# # result = max(x, y, z)
# result = min(x, y, z)

# print(result)

#! Ex. 3

# import math

# x = 9.9

# # print(math.pi)
# # print(math.e)
# # result = math.sqrt(x)
# # result = math.ceil(x)
# result = math.floor(x)


# print(result)

#TODO: Act1 of circumference of a circle

# import math

# radius = float(input("Enter the radius of a circle: "))

# circumference = 2 * math.pi * radius

# print(f"The circumference is: {round(circumference, 2)}cm")

#TODO: Act2 Area of a circle

# import math

# radius = float(input("Enter the radius of a circle: "))

# area = math.pi * pow(radius, 2)

# print(f"The area of the circle is: {round(area, 2)}cm^2")

#TODO: Act3 Find the hypotenuse of the triangle

# import math

# a = float(input("Enter side A: "))
# b = float(input("Enter side B: "))

# c = math.sqrt(pow(a, 2) + pow(b, 2))

# print(f"Side C = {c}")

#! BMI

import random

weigth = float(input("Enter your weight (in kg): "))
height = float(input("Enter you height (in meters): "))

bmi = weigth / pow(height, 2)

if bmi < 18.5:
    category = "Under Weight"
elif 18.5 <= bmi < 24.9:
    category = "Normal Weight"
elif 25.0 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is {round(bmi, 2)}, which is considered {category}")