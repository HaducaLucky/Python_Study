
#! if = Do some code only IF some condition is True
#?      Else do something else

# age = int(input("Enter your age: "))

# if age >= 100:
#     print("You are too old to sign up")
# elif age >= 18:
#     print("You are now signed up!")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("You must be 18+ to sign up")

#TODO: Another Ex.

# response = input("Would you like food? (Y/N): ")

# if response == "Y":
#     print("Have some food!")
# else:
#     print("No food for you!")

#TODO: Another Ex.

# name = input("Enter your name: ")

# if name == "":
#     print("You did not type in your name!")
# else:
#     print(f"Hello {name}")

#TODO: Another Ex.

# online = True

# if online:
#     print("The user is online")
# else:
#     print("The user is offline")

#? Exercise

# age = int(input("How old are you?: "))

# if age < 13:
#     category = "child"
# elif 13 <= age <= 19:
#     category = "teenageer"
# elif 20 <= age <= 59:
#     category = "adult"
# else:
#     category = "senior"

# print(f"You are a {category}")

#? Exercise

# grade = int(input("Enter you grade (0-100): "))

# if 90 <= grade <= 100:
#     print("A")
# elif 80 <= grade <= 89:
#     print("B")
# elif 70 <= grade <= 79:
#     print("C")
# elif 60 <= grade <= 69:
#     print("D")
# elif 0 <= grade <= 59:
#     print("F")
# else:
#     print("Invalid grade! Please enter a grade between 0 and 100 only!")

#? Exercise

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an odd number")

#? Exercise

# password = input("Enter your password: ")

# if password == "password123":
#     print("Access granted")
# else:
#     print("Access denied")

#? Exercise

age = int(input("Enter your age: "))

if age >= 65:
    print("$10")
elif 13 <= age <= 64:
    print("$15")
elif 6 <= age <= 12:
    print("$10")
elif 0 <= age <= 5:
    print("Free")
else:
    print("Enter a proper age!")