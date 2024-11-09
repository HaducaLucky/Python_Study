
#! Python Number Guessing Game

green = "\033[92m"
yellow = "\033[93m"
red = "\033[91m"
blue = "\033[94m"
orange = "\033[38;5;214m"
bold_white = "\033[1;97m"
reset = "\033[0m"

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print()
print(f"{green}🔢 Python Number Guessing Game 🔢{reset}")
print()
print(f"{yellow}Select a number between {reset} {red}{lowest_num}{reset} {yellow}and{reset} {red}{highest_num}{reset}")

while is_running:

    guess = input(f"{blue}Enter your guess: {reset}")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print(f"{red}That number is out of range{reset}")
            print(f"{yellow}Please select a number between{reset} {red}{lowest_num}{reset} {yellow}and{reset} {red}{highest_num}{reset}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"{green}CORRECT!{reset} {yellow}The answer was{reset} {bold_white}{answer}{reset}")
            print(f"{yellow}Number of guesses:{reset} {bold_white}{guesses}{reset}")
            is_running = False
    else:
        print(f"{red}Invalid guess{reset}")
        print(f"{yellow}Please select a number between {reset}{red}{lowest_num}{reset} {yellow}and{reset} {red}{highest_num}{reset}")