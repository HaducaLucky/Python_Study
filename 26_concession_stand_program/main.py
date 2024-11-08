
#! Concession Stand Program
#? dictionary {key:value}

# yellow_text = "\033[33m"
# blue_text = "\033[34m"
# red_text = "\033[31m"
# bold_text = "\033[1m"
# green_text = "\033[32m"
# reset_text = "\033[0m"

# menu = {"pizza": 89.00,
#         "nachos": 75.00,
#         "popcorn": 75.00,
#         "fries": 50.00,
#         "chips": 35.00,
#         "pretzel": 35.00,
#         "soda": 45.00,
#         "lemonade": 45.00}
# cart = []
# total = 0

# print()
# print(f"{blue_text}------ MENU ------{reset_text}")
# for key, value in menu.items():
#     print(f"{yellow_text}{key:10}{reset_text}: {bold_text}₱{value:.2f}{reset_text}")
# print(f"{blue_text}------------------{reset_text}")

# while True:
#     food = input(f"{bold_text}Select an item: ({reset_text}{red_text}q{reset_text} {bold_text}to quit): {reset_text}").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)

# print(f"{blue_text}--- YOUR ORDER ---{reset_text}")
# for food in cart:
#     total += menu.get(food)
#     print(f"{green_text}{food}{reset_text}", end=" ")

# print()
# print(f"{bold_text}Total is: {reset_text}{red_text}₱{total:.2f}{reset_text}")

#TODO: Improve

#! Concession Stand Program
#? dictionary {key:value}

yellow_text = "\033[33m"
blue_text = "\033[34m"
red_text = "\033[31m"
bold_text = "\033[1m"
green_text = "\033[32m"
reset_text = "\033[0m"

menu = {1: {"name": "pizza", "price": 89.00},
        2: {"name": "nachos", "price": 75.00},
        3: {"name": "popcorn", "price": 75.00},
        4: {"name": "fries", "price": 50.00},
        5: {"name": "chips", "price": 35.00},
        6: {"name": "pretzel", "price": 35.00},
        7: {"name": "soda", "price": 45.00},
        8: {"name": "lemonade", "price": 45.00}}

cart = []
total = 0

print()
print(f"{blue_text}------ MENU ------{reset_text}")
for key, item in menu.items():
    print(f"{yellow_text}{key}. {item['name']:<10}{reset_text}: {bold_text}₱{item['price']:.2f}{reset_text}")
print(f"{blue_text}------------------{reset_text}")

while True:
    try:
        choice = input(f"{bold_text}Select an item by number: ({reset_text}{red_text}q{reset_text} {bold_text}to quit): {reset_text}").lower()
        if choice == "q":
            break
        choice = int(choice)
        
        if choice in menu:
            cart.append(choice)
        else:
            print(f"{red_text}Please select a number from the MENU only{reset_text}")
    
    except ValueError:
        print(f"{red_text}Please enter a valid number or 'q' to quit.{reset_text}")

print(f"{blue_text}--- YOUR ORDER ---{reset_text}")
for item_num in cart:
    item = menu[item_num]
    total += item["price"]
    print(f"{green_text}{item['name']}{reset_text}", end=" ")

print()
print(f"{bold_text}Total is: {reset_text}{red_text}₱{total:.2f}{reset_text}")
