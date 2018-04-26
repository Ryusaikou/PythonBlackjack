from BlackJackGame import game_loop, players, getdealer, standard_deck, reset_game

print("Ready to play some BlackJack?")
player = players()
dealer = getdealer()
deck = standard_deck()

while True:
    game_loop(player, dealer, deck)
    if player.credits <= 0:
        print("Out of cash to play with, Better luck next time.")
        break
    if len(deck) < 150:
        deck = standard_deck()
    cont = input('want to play again? (Type yes to continue)')
    if not cont.lower().startswith('y'):
        print("Thanks for Playing")
        break
    else:
        reset_game(player, dealer)
