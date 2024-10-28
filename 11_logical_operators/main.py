
#! logical operators = evalaute multiple conditions (or, and, not)
#?                     or = at least one condition must be True
#?                     and = both conditions must be True
#?                     not = inverts the condition (not Fals, not True)


#TODO: or

# temp = 25
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

#TODO: and

# temp = 14
# is_sunny = True

# if temp >= 28 and is_sunny:
#     print("It is HOT outside 🥵")
#     print("It is SUNNY ☀️")
# elif temp <= 0 and is_sunny:
#     print("It is cold outside 🥶")
#     print("It is SUNNY ☀️")
# elif temp < 28 and temp > 0 and is_sunny:
#     print("It is WARM outside 😊")


#TODO: not

# temp = 0
# is_sunny = False

# if temp >= 28 and is_sunny:
#     print("It is HOT outside 🥵")
#     print("It is SUNNY ☀️")
# elif temp <= 0 and is_sunny:
#     print("It is cold outside 🥶")
#     print("It is SUNNY ☀️")
# elif temp < 28 and temp > 0 and is_sunny:
#     print("It is WARM outside 😊")
#     print("It is SUNNY ☀️")
# elif temp >= 28 and not is_sunny:
#     print("It is HOT outside 🥵")
#     print("It is CLOUDY ☁️")
# elif temp <= 0 and not is_sunny:
#     print("It is cold outside 🥶")
#     print("It is CLOUDY ☁️")
# elif temp < 28 and not temp > 0 and is_sunny:
#     print("It is WARM outside 😊")
#     print("It is CLOUDY ☁️")

#* Exercise1 Age and Membership Check

# age = 12
# is_member = True

# if age >= 18 and is_member:
#     print("You can enter the event ✅")
# else:
#     print("You cannot enter ❌")

#? v2

# age = int(input("Enter you age: "))
# is_member = input("Do you have a membership (Y/N): ").strip().upper()

# if age >= 18 and is_member == "Y":
#     print("You can enter the event ✅")
# else:
#     print("You cannot enter ❌")
    
#* Exercise2 Multiple Conditions Check

# num1 = int(input("Enter the 1st number: "))
# num2 = int(input("Enter the 2nd number: "))
# num3 = int(input("Enter the 3rd number: "))

# if num1 >= 0 and num2 >=0 and num3 >= 0:
#     print("All numbers are positive")
# else:
#     print("At least one number is negative")

#* Exercise3 Fruit Choice

# fruit = input("What is your favorite fruit: ")

# if fruit == "apple" or fruit == "banana":
#     print("Great choice!")
# else:
#     print(f"{fruit} that's a nice fruit, too!")