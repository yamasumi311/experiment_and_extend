import random

numbers = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J','Q','K']
suits = ['Dia', 'Spade', 'Clover', 'Heart']
my_cards = [] # user's deck
co_cards = [] # computer's deck


def make_cards():
    number = random.choice(numbers)
    suit = random.choice(suits)
    card = number + '-' + suit
    return card


def find_card_order(card1, card2):
    if card1 == card2:
        return 'same' #picked the same card
    cpos1 = card1[0: card1.find('-')] # Array slicing [start:end:step]
    cpos2 = card2[0: card2.find('-')]
    order1 = numbers.index(cpos1)
    order2 = numbers.index(cpos2)
    if order1 > order2:
        return 'higher'
    elif order1 < order2:
        return 'lower'
    else: #same cardno but not same suit
        return 'same'


def create_deck(maisu):
    for i in range(maisu):
        my_cards.append(make_cards())


# 1 ask user to choose numbers of cards to play
maisu = int(input('How many cards do you want to play?: '))
create_deck(maisu)
print(my_cards)



