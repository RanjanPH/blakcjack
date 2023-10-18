#! first function
import random, sys
from char import HEARTS, DIAMONDS, SPADES, CLUBS


def getBet(maxBet):
    while True:
        print(f"How much do you bet? (1-{maxBet},or QUIT)")
        bet = input(">").upper().strip()
        if bet == "QUIT":
            print("Thanks for playing !")
            sys.exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet


def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))

        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))
    random.shuffle(deck)

    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    print()

    if showDealerHand:
        print("DEALER: ", getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("DEALER:???")
        displayCards([BACKSIDE] + dealerHand[1:])

    print("PLAYER: ", getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    value = 0
    numberOfAces = 0

    for card in cards:
        rank = card[0]
        if rank == "A":
            numberOfAces += 1
        elif rank in ("K", "Q", "J"):
            value += 10
        else:
            value += int(rank)

    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10

    return


def displayCards(cards):
    rows = ["", "", "", "", ""]
    for i, card in enumerate(cards):
        rows[0] += "___"
        if card == BACKSIDE:
            rows[1] += "|## | "
            rows[2] += "|###| "
            rows[3] += "|_##| "
        else:
            rank, suit = card
            rows[1] += "|{} | ".format(rank.ljust(2))
            rows[2] += "| {} | ".format(suit)
            rows[3] += "|_{}| ".format(rank.rjust(2, "_"))

    for row in rows:
        print(row)


def getMove(playerHand, money):
    while True:
        moves = ["(H)it", "(S)tand"]

        if len(playerHand) == 2 and money > 0:
            moves.append("(D)ouble down")

        movePrompt = ",".join(moves) + "> "
        move = input(movePrompt).upper()
        if move in ("H", "S"):
            return move

        if move == "D" and "(D)ouble down" in moves:
            return move
