
#! function = A block of reusable code
#?            place () after the function name to invoke it

# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age} years old!")
#     print("Happy birthday to you!")
#     print()

# happy_birthday("Linkx", 20)
# happy_birthday("Steve", 30)
# happy_birthday("Joe", 40)

#! return = stament used to end a function
#!          and send a result back to the caller

# def add(x, y):
#     z = x + y
#     return z

# def subtract(x, y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x * y
#     return z

# def divide(x, y):
#     z = x / y
#     return z

# print(add(1, 2))
# print(subtract(1, 2))
# print(multiply(2, 6))
# print(round(divide(2, 6), 2))

#TODO: Exercise to create full name

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("linkx", "mere")

print(full_name)