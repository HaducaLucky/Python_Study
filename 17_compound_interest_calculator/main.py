
#! Python compound interest calculator

# princple = 0
# rate = 0
# time = 0

# while princple <= 0:
#     princple = float(input("Enter the principle amount: "))
#     if princple <= 0:
#         print("Principle can't be less than or equal to zero")

# while rate <= 0:
#     rate = float(input("Enter the interest rate: "))
#     if rate <= 0:
#         print("Interest rate can't be less than or equal to zero")

# while time <= 0:
#     time = int(input("Enter the time in years: "))
#     if time <= 0:
#         print("Time can't be less than or equal to zero")

# total = princple * pow((1 + rate / 100), time)
# print(f"Balance after {time} year/s: ${total:.2f}")

#* Another approach

princple = 0
rate = 0
time = 0

while True:
    princple = float(input("Enter the principle amount: "))
    if princple < 0:
        print("Principle can't be less zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero")
    else:
        break

total = princple * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")