from random import randint


class Card(object):
    def __init__(self, suit, value):
        self.isAce = False
        if value == 1:
            self.face = "Ace"
            self.value = 1
            self.isAce = True
        if 2 <= value <= 10:
            self.face = str(value)
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
        self.cardname = f"{self.face} of {self.suit}"


def getdeck(numofdecks):
    returnDeck = []
    for deck in range(0, numofdecks):
        suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        for suit in suits:
            for x in range(1, 14):
                returnDeck.append(Card(suit, x))
    return ShuffleDeck(returnDeck)


def ShuffleDeck(Deck):
    returndeck = []
    leng = len(Deck) - 1
    for x in range(0, len(Deck)):
        rng = randint(0, leng)
        returndeck.append(Deck.pop(rng))
        leng = leng - 1
    return returndeck
