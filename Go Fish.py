"""
LESSON: 6.3 - Complex Parameters
EXERCISE: Go Fish
"""

#### ---- LIBRARIES ---- ####
import random


#### -------------------- ####
#### ---- DRAW CARDS ---- ####
#### -------------------- ####
def draw_cards(deck, hand, num_cards=5):

    # Get as many cards as requested
    for i in range(num_cards):

        # If deck is empty, stop drawing cards
        if len(deck) == 0:
            break

        # Otherwise, move top card from deck to hand
        hand.append(deck[0])
        deck.remove(deck[0])


#### ----------------------- ####
#### ---- DISPLAY CARDS ---- ####
#### ----------------------- ####
def display_cards(hand):

    hand_string = ""

    # Go through cards
    for card in hand:

        # Add the number
        hand_string += get_card_value(card)

        # Add the suit
        hand_string += " "
        if card[len(card) - 1] == "H":
            hand_string += "(hearts)"
        if card[len(card) - 1] == "D":
            hand_string += "(diamonds)"
        if card[len(card) - 1] == "C":
            hand_string += "(clubs)"
        if card[len(card) - 1] == "S":
            hand_string += "(spades)"

        # Add comma & space
        if not (hand.index(card) == len(hand) - 1):
            hand_string += ", "

    return hand_string


#### -------------------- ####
#### ---- TAKE CARDS ---- ####
#### -------------------- ####
def take_cards(take_from, give_to, card_value):
    cards_to_transfer = []

    # Check if cards are in hand
    for card in take_from:
        if get_card_value(card) == card_value:
            cards_to_transfer.append(card)

    # Move cards from one hand to the other
    for card in cards_to_transfer:
        take_from.remove(card)
        give_to.append(card)

    # Return number of cards transferred
    return len(cards_to_transfer)


#### -------------------------- ####
#### ---- CHECK FOR POINTS ---- ####
#### -------------------------- ####
def check_for_points(hand):
    points = 0

    # Look for matching cards
    for i in range(len(hand)):
        if i >= len(hand):
            break

        matched_cards = []
        for check_card in hand:
            if get_card_value(hand[i]) == get_card_value(check_card):
                matched_cards.append(check_card)

        # Check if you found a set of 4
        if len(matched_cards) == 4:
            points += 1
            print("Matched " + get_card_value(matched_cards[0]) + "'s")

            # Remove matched cards
            for card in matched_cards:
                hand.remove(card)

    return points


#### ------------------ ####
#### ---- NEW DECK ---- ####
#### ------------------ ####
def new_deck():
    suits = ["-H", "-D", "-S", "-C"]
    deck = []

    # For each suit, put in all numbered cards
    for suit in suits:
        for i in range(2, 11):
            deck.append(str(i) + suit)

        # Add the face cards & aces
        deck.append("J" + suit)
        deck.append("Q" + suit)
        deck.append("K" + suit)
        deck.append("A" + suit)

    # Shuffle deck
    random.shuffle(deck)
    return deck


#### ------------------------ ####
#### ---- GET CARD VALUE ---- ####
#### ------------------------ ####
def get_card_value(card):
    val = ""
    for character in card:
        if character != "-":
            val += character
        else:
            break

    return val


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

#### ---- SETUP ---- ####
# Variables
draw_deck = new_deck()
player_hand = []
computer_hand = []
player_points = 0
computer_points = 0
player_turn = True

# Draw Starting Hands
draw_cards(draw_deck, player_hand)
draw_cards(draw_deck, computer_hand)


#### ---- MAIN LOOP ---- ####
while len(draw_deck) > 0 or (len(player_hand) and len(player_hand)):

    # Turn Setup
    print()

    if player_turn:
        print("--- PLAYER'S TURN ---")
        active_hand = player_hand
        other_hand = computer_hand
    else:
        print("--- COMPUTER'S TURN ---")
        active_hand = computer_hand
        other_hand = player_hand

    print()
    print("Player Points: " + str(player_points))
    print("Computer Points: " + str(computer_points))
    print()


    #### ---- DO YOU HAVE ANY... ---- ####
    # Current player asks for cards
    got_cards = True
    while got_cards:

        # If either player is empty, draw more cards
        if len(player_hand) == 0:
            draw_cards(draw_deck, player_hand)

        if len(computer_hand) == 0:
            draw_cards(draw_deck, computer_hand)

        # Show player's current hand
        print("Player Hand: " + display_cards(player_hand))

        # Ask for cards
        if player_turn:
            card_to_get = input("Do you have any... (Enter 2-10, J, Q, K, or A): ")
        else:
            card_to_get = get_card_value(random.choice(computer_hand))
            print("Do you have any " + str(get_card_value(card_to_get)) + "'s ?")

        # Transfer cards from one person to another
        num_cards = take_cards(other_hand, active_hand, card_to_get)
        print("Got " + str(num_cards) + " cards")
        print()

        if num_cards == 0:
            got_cards = False

    # Check for Points
    points_earned = check_for_points(active_hand)
    if player_turn:
        player_points += points_earned
    else:
        computer_points += points_earned


    #### ---- GO FISH ---- ####
    # Current player draws card
    print("Go fish!")
    draw_cards(draw_deck, active_hand, 1)

    # Display new card for player only
    if player_turn and len(player_hand) > 0:
        card_str = player_hand[len(player_hand) - 1]
        card_str_formatted = display_cards([card_str])
        print("Got " + card_str_formatted)

    # Check for Points
    points_earned = check_for_points(player_hand)
    if player_turn:
        player_points += points_earned
    else:
        computer_points += points_earned

    # Switch players
    player_turn = not player_turn

    input("(Press enter to continue)")
    print()
    print("--------------------------")


#### ---- FINAL WINNER ---- ####
# Print final scores
print("GAME OVER")
print()
print("FINAL SCORE:")
print("   Player: " + str(player_points))
print("   Computer: " + str(computer_points))
print()

# Print winners
if player_points > computer_points:
    print("PLAYER WINS!")
else:
    print("COMPUTER WINS!")


# Turn in your Coding Exercise.
