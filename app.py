import random, sys

from char import BACKSIDE
from fun_jack import getBet, getDeck, displayHands, getHandValue, displayCards, getMove




def main():
    print(
        """BlackJack 
          RULES: 
          Try to get as close to 21 without going over.
          Kings, Queens, and Jacks are worth 10 points.
          Aces are worth 1 or 11 points.
          Cards 2 through 10 are worth their face value.
          (H)it to take another card.
          (S)tand to stop taking cards.
          On your first play, you can (D)ouble down to increase your bet
          but must hit exactly one more time before standing.
          In case of a tie, the bet is returned to the player.
          The dealer stops hitting at 17."""
    )

    money = 5000
    while True:
        if money <= 0:
            print("Broke man")
            print("Go home")
            sys.exit()

    print("Money: ", money)

    bet = getBet(money)

    deck = getDeck()
    dealerHand = [deck.pop(), deck.pop()]
    playerHand = [deck.pop(), deck.pop()]

    print("Bet: ", bet)
    #! Players action
    while True:
        displayHands(playerHand, dealerHand, False)

        if getHandValue(playerHand) > 21:
            break

        move = getMove(playerHand, money - bet)

        if move == "D":
            additionalBet = getBet(min(bet, (money - bet)))
            bet += additionalBet
            print(f"Bet increased to {bet}.")
            print("Bet: ", bet)

        if move == ("H", "D"):
            newCard = deck.pop()
            rank, suit = newCard
            print(f"You drew a {rank} of {suit}")
            playerHand.append(newCard)

            if getHandValue(playerHand) > 21:
                continue

        if move == ("S", "D"):
            break

    #! dealers action

    if getHandValue(playerHand) <= 21:
        while getHandValue(dealerHand) < 17:
            print("Dealer Hits...")
            dealerHand.append(deck.pop())
            displayHands(playerHand, dealerHand, False)

            if getHandValue(dealerHand) > 21:
                break
            input("Press Enter to continue...")
            print("\n\n")

    #! final hand

    displayHands(playerHand, dealerHand, True)
    playerValue = getHandValue(playerHand)
    dealerValue = getHandValue(dealerHand)

    #! handling whether the player won or lose or tie
    if dealerValue > 21:
        print(f"Dealer Bust! You win {bet}!")

    elif (playerValue > 21) or (playerValue < dealerValue):
        print("Chal Hatt, YOu lose!")

        money -= bet
    elif playerValue > dealerValue:
        print("Badhai HO Badhai , You Won!")
        money += bet

    elif playerValue == dealerValue:
        print("It\s a tie, the bet is returned")

        input("Press Enter to continue....")
        print("\n\n")
        
    


if __name__ == "__main__":
    main()
