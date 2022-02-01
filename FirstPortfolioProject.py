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
                card = 1
            card = 11
        total += card
    return total


def hit(hand):
    hand.append(deck.pop())
    return hand


def blackjack(player_hand, dealer_hand):
    if total(player_hand) == 21 and total(dealer_hand) == 21:
        print("It's a tie. You both have blackjack!")
    elif total(player_hand) == 21:
        print("You win! You have blackjack!")
    elif total(dealer_hand) == 21:
        print("You lose. The dealer has blackjack.")


def bust(player_hand, dealer_hand):
    if total(player_hand) > 21:
        print("Bust! You lose.")
    elif total(dealer_hand) > 21:
        print("The dealer busted. You win!")


def scoring(player_hand, dealer_hand):
    if total(player_hand) > total(dealer_hand):
        print("Your total is higher than the dealer's. You win!")
    elif total(player_hand) < total(dealer_hand):
        print("The dealer's total is higher than yours. You lose.")


def play_game():
    player_hand = deal()
    dealer_hand = deal()
    print(f"Dealer's hand: {dealer_hand[0]}")
    print(f"Your hand: {player_hand} for a total of {total(player_hand)}")
    blackjack(player_hand, dealer_hand)
    command = ""
    while command != "quit":
        command = input("Would you like to hit, stay, or quit the game? \n> ").lower()
        if command == "hit" and total(player_hand) < 21:
            hit(player_hand)
            print(f"Your hand: {player_hand} for a total of {total(player_hand)}")
            bust(player_hand, dealer_hand)
        elif command == "hit" and total(player_hand) == 21:
            print("You already have 21. Either stay or quit.")
        elif command == "stay":
            print(f"Dealer's hand: {dealer_hand} for a total of {total(dealer_hand)}")
            while total(dealer_hand) < 17:
                hit(dealer_hand)
                print(f"Dealer's hand: {dealer_hand} for a total of {total(dealer_hand)}")
            bust(player_hand, dealer_hand)
            blackjack(player_hand, dealer_hand)
            if total(player_hand) < 21 and total(dealer_hand) < 21:
                scoring(player_hand, dealer_hand)
        elif command == "quit" or "quit game" or "quit the game":
            print("Goodbye")
            break
        else:
            print("Error: please choose either hit, stay, or quit.")


play_game()
