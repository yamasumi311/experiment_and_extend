import random

from constant import numbers, suits


def scoring(result, my_score, co_score):
    if result == 'higher':
        my_score += 1
    elif result == 'lower':
        co_score += 1
    return my_score, co_score

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
        print("You won this turn!")
        return 'higher'
    elif order1 < order2:
        print("You lost this turn.")
        return 'lower'
    else: #same cardno but not same suit
        print("It's a tie!")
        return 'same'


def create_deck(maisu, whoes):
    for i in range(maisu):
        whoes.append(make_cards())
