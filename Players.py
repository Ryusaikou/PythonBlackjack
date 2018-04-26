class Player:
    def __init__(self, name, credits_):
        self.name = name
        self.credits = credits_
        self.hasWon = False
        self.hasLost = False
        self.bet = 0
        self.hand = []
