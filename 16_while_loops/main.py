
#! while loop = execute some code WHILE some conditio remains true

# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")

# print(f"Hello {name}")

#* another ex.

# age = int(input("Enter you age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter you age: "))

# print(f"You are {age} years old")

#* another ex. using NOT

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")

# print("Bye")

#* another ex. OR

num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"Your number is {num}")