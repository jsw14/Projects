#Blackjack terminal game
#prints one dealer card and prints two player cards
#input stay or hit
#print dealer cards on stay

import random

print("""
Hello there! You are about to play Blackjack. The rules are simple: you are playing against the dealer. 
The goal is to have a sum of card values closest to 21 but not over or else you bust and automatically lose that turn. 
Each turn you and the dealer are given two cards, but one of the dealer's cards is hidden until you finish your actions for that turn.
Based on the cards you have and the one dealer card shown, you can either decide to hit (get another card to add to your total this turn)
or stay (stay with your current cards). You can hit as many times as you want until you bust (have a sum of over 21) or choose to stay.
Once you stay, it is the dealers turn to reveal the hidden card and draw cards until they have a total of 17 or higher. 
If the dealer busts, you win. Otherwise, who ever has the largest total wins. 
"""
)

#first need a deck of cards to draw from
deck = [2, 3, 4, 5, 6 ,7, 8, 9, 10, "J", "Q", "K", "A" ] * 4

#give starting cards to player and dealer
#need a list to hold the cards

def deal():
    hand = []
    for i in range(2):
        random.shuffle(deck)
        hand.append(deck.pop())
    return hand


def total(hand):
    total = 0
    for card in hand:
        if card == "J":
            card = 10
        elif card == "Q":
            card = 10
        elif card == "K":
            card = 10
        elif card == "A":
            if total >= 11:
                card == 1
            card == 11
        total += card
    return total

print(total(deal()))
