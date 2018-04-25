from typing import List
import random


class Card(object):
    face = ""
    suit = ""
    value = 0
    name = ""
    isAce = False

    def __init__(self, facev, suit, value):
        if value == 1:
            self.face = "Ace"
            self.value = 1
            self.isAce = True
        if 2 <= value <= 10:
            self.face = facev
            self.value = value
        if value == 11:
            self.face = "Jack"
            self.value = 10
        if value == 12:
            self.face = "Queen"
            self.value = 10
        if value == 13:
            self.face = "King"
            self.value = 10

        self.suit = suit
        self.name = self.face + " of " + self.suit


def getdeck(numofdecks):
    # type: (List[Card]) -> object
    returnDeck = []  # type: List[Card]
    for deck in range(0, numofdecks):
        suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        for suit in suits:
            for x in range (1, 14):
                returnDeck.append(Card(str(x), suit, x))
    return returnDeck


def GetRand(x, y):
    return random.randint(x, y)


def ShuffleDeck(Deck):
    returnDeck = []
    leng = len(Deck)
    lengt = len(Deck) - 1
    for x in range(0, leng):
        RNG = random.randint(0, lengt)
        returnDeck.append(Deck.pop(RNG))
        lengt = lengt - 1
    return returnDeck
