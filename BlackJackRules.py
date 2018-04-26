def check_bet(player):
    try:
        bet = input(f"How Much would you like to bet {player.name}?")
        player.bet = int(bet)

    except ValueError:
        print(f"You have entered something that is not a number, this game does not accept {bet}'s")
        return False
    if player.bet > player.credits:
        print("You don't have enough credits for that bet")
        return False
    else:
        print(f"You have bet {str(player.bet)} Good Luck!")
        player.credits -= player.bet
        return True


def hit_me(deck, player):
    print(f"{player.name} has drawn the {deck[0].cardname}")
    player.hand.append(deck.pop(0))


def gameplay(player, deck, is_dealer):
    if is_dealer:
        while hand_value(player.hand) < 17:
            hit_me(deck, player)
            check_hand(player, False)
            print(str(hand_value(player.hand)))
        if hand_value(player.hand) <= 21:
            print(f"Dealer will stand with a hand value of {str(hand_value(player.hand))}")
        return True
    else:
        while hand_value(player.hand) <= 21:
            wannahit = input(
                f"Your Hand Total is {str(hand_value(player.hand))} Would you like to hit or stand (Type answer)")
            if wannahit.lower() == "hit":
                hit_me(deck, player)
                print(f"That puts your hand value at {str(hand_value(player.hand))}")
                check_hand(player, False)
            if wannahit.lower() == "stand":
                print(f"You have chosen to stand with a hand value of {str(hand_value(player.hand))}")
                break
            if wannahit.lower() == "split":
                print("I haven't implemented split, too lazy")
            if wannahit.lower() == "one" or wannahit.lower() == "answer":
                print("Ha fuckin Ha Smart Ass, Fine... I'll choose for you")
                if hand_value(player.hand) > 15:
                    print("I hope you bust")
                    hit_me(deck, player)
                    check_hand(player, False)
                    if hand_value(player.hand) > 21:
                        print("YOU BUST! HA HA That's what you Get!")
                    if hand_value(player.hand) == 21:
                        print("I hate you...")
                else:
                    print("You gonna Stand")
                    break
            if wannahit.lower() != "stand" and wannahit.lower() != "hit":
                print("Only stand and hit are recognized commands, type one")
        return True


def hand_value(hand):
    returnvalue = 0
    for x in hand:
        if x.isAce and 11 + returnvalue <= 21:
            returnvalue += 11
        else:
            returnvalue += x.value
    return returnvalue


def check_hand(player, firstHand):
    handValue = hand_value(player.hand)
    print(f"The current hand value is {handValue}")
    if handValue == 21 and firstHand:
        print("BlackJack! That Pays 2:1!")
        player.hasWon = True
    if handValue > 21:
        print(f"{player.name} Bust!")
        player.hasLost = True


def game_over(player, dealer, payout, end):
    if player.hasWon:
        print(f"Your payout is {player.bet * payout}")
        player.credits += player.bet * payout
        return True
    if player.hasLost:
        print("Better luck next time!")
        return True
    if dealer.hasWon:
        print("The Dealer drew 21, You Lose")
        return True
    if dealer.hasLost:
        print(f"You Win! Payout is {str(player.bet * payout)}")
        player.credits += player.bet * payout
        return True
    if end:
        if hand_value(player.hand) > hand_value(dealer.hand):
            print(f"You Win!, go Payout is {str(player.bet * payout)}")
            player.credits += player.bet * payout
            return True
        else:
            print("Dealer wins, Better luck next time")
            return True
    return False
