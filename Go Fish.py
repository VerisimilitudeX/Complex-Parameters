#### ---- LIBRARIES ---- ####
import random

#### -------------------- ####
#### ---- DRAW CARDS ---- ####
#### -------------------- ####
def draw_cards(deck, hand, num_cards=5):
    for i in range(num_cards):
        if len(deck) == 0:
            break
        hand.append(deck[0])
        deck.remove(deck[0])

#### ----------------------- ####
#### ---- DISPLAY CARDS ---- ####
#### ----------------------- ####
def display_cards(hand):
    hand_string = ""
    for card in hand:
        hand_string += get_card_value(card)
        hand_string += " "
        if card[len(card) - 1] == "H":
            hand_string += "(hearts)"
        if card[len(card) - 1] == "D":
            hand_string += "(diamonds)"
        if card[len(card) - 1] == "C":
            hand_string += "(clubs)"
        if card[len(card) - 1] == "S":
            hand_string += "(spades)"
        if not (hand.index(card) == len(hand) - 1):
            hand_string += ", "
    return hand_string

#### -------------------- ####
#### ---- TAKE CARDS ---- ####
#### -------------------- ####
def take_cards(take_from, give_to, card_value):
    cards_to_transfer = []

    for card in take_from:
        if get_card_value(card) == card_value:
            cards_to_transfer.append(card)

    for card in cards_to_transfer:
        take_from.remove(card)
        give_to.append(card)

    return len(cards_to_transfer)

#### -------------------------- ####
#### ---- CHECK FOR POINTS ---- ####
#### -------------------------- ####
def check_for_points(hand):
    points = 0

    for i in range(len(hand)):
        if i >= len(hand):
            break

        matched_cards = []
        for check_card in hand:
            if get_card_value(hand[i]) == get_card_value(check_card):
                matched_cards.append(check_card)

        if len(matched_cards) == 4:
            points += 1
            print("Matched " + get_card_value(matched_cards[0]) + "'s")

            for card in matched_cards:
                hand.remove(card)

    return points

#### ------------------ ####
#### ---- NEW DECK ---- ####
#### ------------------ ####
def new_deck():
    suits = ["-H", "-D", "-S", "-C"]
    deck = []

    for suit in suits:
        for i in range(2, 11):
            deck.append(str(i) + suit)

        deck.append("J" + suit)
        deck.append("Q" + suit)
        deck.append("K" + suit)
        deck.append("A" + suit)

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
draw_deck = new_deck()
player_hand = []
computer_hand = []
player_points = 0
computer_points = 0
player_turn = True

draw_cards(draw_deck, player_hand)
draw_cards(draw_deck, computer_hand)

#### ---- MAIN LOOP ---- ####
while len(draw_deck) > 0 or (len(player_hand) and len(player_hand)):
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
    got_cards = True
    while got_cards:
        if len(player_hand) == 0:
            draw_cards(draw_deck, player_hand)
        if len(computer_hand) == 0:
            draw_cards(draw_deck, computer_hand)
        print("Player Hand: " + display_cards(player_hand))
        if player_turn:
            card_to_get = input("Do you have any... (Enter 2-10, J, Q, K, or A): ")
        else:
            card_to_get = get_card_value(random.choice(computer_hand))
            print("Do you have any " + str(get_card_value(card_to_get)) + "'s ?")

        num_cards = take_cards(other_hand, active_hand, card_to_get)
        print("Got " + str(num_cards) + " cards")
        print()

        if num_cards == 0:
            got_cards = False

    points_earned = check_for_points(active_hand)
    if player_turn:
        player_points += points_earned
    else:
        computer_points += points_earned

    #### ---- GO FISH ---- ####

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
