import random
import time

from functions import scoring, find_card_order, create_deck

my_cards = [] # user's deck
co_cards = [] # computer's deck

my_score = 0
co_score = 0

# 1 ask user to choose maisu and reveal the deck
maisu = int(input('How many cards do you want to play?: '))
create_deck(maisu, my_cards)
print("Your deck:")
for (i, card) in enumerate(my_cards, start=0):
    print(f"{i}: {card}")

# 2 make a computer deck
create_deck(maisu, co_cards)

# 3 choose which card to play
print('Which card do you want to play first?')
index = int(input('Choose the index number: '))
my_card = my_cards[index]
print(f"You play [{my_card}]")

# 4 computer's turn
print("Computer's turn")
time.sleep(1)
index = random.randint(0, maisu - 1)
co_card = co_cards[index]
print(f"Computer plays [{co_card}]")

# compare result
result = find_card_order(my_card, co_card)
my_score, co_score = scoring(result, my_score, co_score)
print(f"Your score is: {my_score}")
print(f"Computer's score is: {co_score}")


