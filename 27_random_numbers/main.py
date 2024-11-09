
import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# number = random.randint(1, 20)
# number = random.randint(low, high)
# number = random.random() #? show float between 0 and 1
# option = random.choice(options) #? Useful. if we want a random element
random.shuffle(cards) #? use .shuffle to SHUFFLE

print(cards)