from BlackJackRules import hit_me, check_hand, check_bet, game_over, gameplay
from Players import Player
from Deck import getdeck

def players():
    name = input("What is your Name?")
    startcred = 1000
    return Player(name, startcred)


def getdealer():
    name = "Dealer"
    startcred = 0
    return Player(name, startcred)


def standard_deck():
    return getdeck(5)


def game_loop(player, dealer, deck):
        player_loop(player, dealer, deck)
        game_over(player, dealer, 2, False)
        dealer_loop(player, dealer, deck)
        game_over(player, dealer, 2, True)


def player_loop(player, dealer, deck):
    while True:
        if check_bet(player):
            break
    hit_me(deck, player)
    hit_me(deck, player)
    check_hand(player, True)
    game_over(player, dealer, 3, False)  # Checking for blackjack
    while True:
        if gameplay(player, deck, False):
            break


def dealer_loop(player, dealer, deck):
    hit_me(deck, dealer)
    hit_me(deck, dealer)
    check_hand(dealer, False)
    game_over(player, dealer, 0, False)  # Checking for blackjack
    while True:
        if gameplay(dealer, deck, True):
            break


def reset_game(player, dealer):
    player.hand.clear()
    dealer.hand.clear()
    player.hasWon = False
    player.hasLost = False
    dealer.hasWon = False
    dealer.hasLost = False
