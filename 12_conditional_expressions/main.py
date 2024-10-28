
#! condiotional expression = A one-line shortcut if-else statement (ternary operator)
#?                           Print or assign one of two values based on a condition
#*                           X if condition else Y

# num = 4
# a = 6
# b = 7
# age = 13
# temp = 20
# user_role = "guest"


# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "HOT" if temp > 20 else "COLD"
# access_level = "Full Access" if user_role == "admin" else "Limited Access"

# print(access_level)

#TODO: Ex. 1

# age = int(input("How old are you?: "))
# has_license = input("Do you have a license (Y/N): ")

# ready = "Eligible to drive" if age >= 18 and has_license == "Y" else "Not eligible to drive"

# print(ready)

#TODO: Ex. 2

# year = int(input("Enter a year: "))

# leap_year = "Leap year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not a leap year"

# print(leap_year)

num = int(input("Enter a number: "))

check = "It is divisible by 3 and 5" if num % 3 == 0 or num % 5 == 0 else "It is not divisible by 3 and 5"

print(check)