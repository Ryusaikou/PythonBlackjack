from Deck import *
from RulesEngine import *

PlayDeck = ShuffleDeck(getdeck(5))  # type: List[Card]
credits = 1000
keepPlaying = True
Hand = []
Dealer = []
while keepPlaying:
    hasLost = False
    hasWon = False
    bet = input("How much would you like to bet?")
    if Checkbet(credits, bet):
        credits = credits - int(bet)
    else:
        continue

    # Deal
    Hand.append(HitMe(PlayDeck, False))
    Hand.append(HitMe(PlayDeck, False))
    if CheckState(HandValue(Hand)):
        print("BlackJack! That's a 2:1 payout! With your bet of " + str(bet) + " that gets you " + str(int(bet) * 3) +
              " Credits!")
        credits += int(bet) * 3
        Hand.clear()
        continue
    hitloop = True
    while hitloop:
        wannahit = input("Your Hand Total is " + str(HandValue(Hand)) + " Would you like to hit or stand (Type answer)")
        if wannahit.lower() == "hit":
            Hand.append(HitMe(PlayDeck, False))
            print("That puts your hand value at " + str(HandValue(Hand)))
            if isBust(HandValue(Hand)):
                print("BUST! Sorry try again")
                hitloop = False
                hasLost = True
        if wannahit.lower() == "stand":
            print("You have chosen to stand with a hand value of " + str(HandValue(Hand)))
            hitloop = False
        if wannahit.lower() == "split":
            print("I haven't implemented split, too lazy")
        if wannahit.lower() == "one" or wannahit.lower() == "answer":
            print("Ha fuckin Ha Smart Ass, Fine... I'll choose for you")
            if HandValue(Hand) > 15:
                print("I hope you bust")
                Hand.append(HitMe(PlayDeck, False))

                if HandValue(Hand) > 21:
                    print("YOU BUST! That's what you Get!")
                    hasLost = True
                    hitloop = False
                    continue
                if HandValue(Hand) == 21:
                    print("I hate you...")
            else:
                print("You gonna Stand")
                hitloop = False
                continue
        if wannahit.lower() != "stand" and wannahit.lower() != "hit":
                print("Only stand and hit are recognized commands, type one")

    if hasLost:
        Hand.clear()
        continue
    print("Lets see what the dealer has to say about that")
    Dealer.append(HitMe(PlayDeck, True))
    Dealer.append(HitMe(PlayDeck, True))
    dealLoop = True
    while dealLoop:
        if HandValue(Dealer) > 21:
            print("Dealer Bust!")
            hasWon = True
            dealLoop = False
            continue
        if HandValue(Dealer) == 21:
            print("Dealer has 21, You lose")
            dealLoop = False
            hasLost = True
            continue
        if HandValue(Dealer) > 17:
            dealLoop = False
            print("Dealer will stand with a hand value of " + str(HandValue(Dealer)))
            continue
        else:
            Dealer.append(HitMe(PlayDeck, True))

    if HandValue(Hand) > HandValue(Dealer):
        if not hasLost:
            hasWon = True
    else:
        if not hasWon:
            hasLost = True
    if hasWon:
        print("You Win " + str(int(bet) * 2) + " Credits!")
        credits += int(bet) * 2
    if hasLost:
        print("Better luck next time")
    Hand.clear()
    if credits <= 0:
        keepPlaying = False
        continue

print("Thanks for playing!")
