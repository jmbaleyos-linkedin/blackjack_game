import art
import random

suits = {"♠": ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
         "♥": ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
         "♦": ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
         "♣": ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]}

card_on_hands = {
    "player": {
        "cards":{},
        "total": 0
    },
    "dealer": {
        "cards": {},
        "total": 0
    }
}

def card_remover(suit_number):
    """ It accepts the Lists Ranks and Suits.
    It checks if the chosen random suit or number count is still above 0."""
    suit = random.choice(list(suit_number.keys()))
    number = random.choice(suit_number[suit])
    suits[suit].remove(number)
    return suit, number

def card_picker(hand):
    """Picks a random suit, and number"""
    random_suit, random_number = card_remover(suits)
    card_on_hands[hand]["cards"][random_number] = art.make_card(random_number, random_suit)
    card_on_hands[hand]["total"] = number_checker(hand)

def number_checker(hand):
    """Checks if the picked random number is Ace, Jack, Queen, or King. Then returns that equivalent value."""
    total = 0
    ace = 0
    for number in card_on_hands[hand]["cards"].keys():
        if number == "A":
            ace += 1
        elif number in ["J", "Q", "K"]:
            total += 10
        else:
            total += int(number)

    for _ in range(ace):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1
    return total

def display_cards(hand):
    """Displays the Cards ASCII arts."""
    for row in zip(*card_on_hands[hand]["cards"].values()):
        print(" ".join(row))
    print(f"Score {card_on_hands[hand]["total"]}.")

def cards_reset():
    """Resets the entire deck."""
    full_deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    for suit in suits:
        suits[suit] = full_deck.copy()

def card_on_hand_reset():
    """Resets the cards on the player's and dealer's hand."""
    card_on_hands["player"] = {"cards": {},"total": 0}
    card_on_hands["dealer"] = {"cards": {}, "total": 0}

play_blackjack = True
while play_blackjack:
    card_on_hand_reset()
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_game == 'y':
        print(art.logo)
        card_picker("dealer")
        more_cards = True
        while more_cards:
            card_picker("player")
            display_cards("player")
            display_cards("dealer")

            if card_on_hands["player"]["total"] <= 21:
                wrong_input = True
                while wrong_input:
                    add_cards = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                    if add_cards == 'n':
                        print("Your final hand:")
                        display_cards("player")
                        wrong_input = False
                        more_cards = False
                    elif add_cards == 'y':
                        wrong_input = False
                    else:
                        print("Please enter 'y' for Yes, and 'n' for No only.")
            else:
                print("Your final hand:")
                display_cards("player")
                more_cards = False

        more_cards = True
        while more_cards:
            if card_on_hands["player"]["total"] <= 21:
                if card_on_hands["dealer"]["total"] <= 16 or card_on_hands["player"]["total"] > card_on_hands["dealer"]["total"]:
                    card_picker("dealer")
                else:
                    more_cards = False
            else:
                more_cards = False

        print("Computer's final hand:")
        display_cards("dealer")

        if card_on_hands["player"]["total"] > 21:
            print("You went over 21. You lose!")
        elif card_on_hands["player"]["total"] > card_on_hands["dealer"]["total"] or card_on_hands["dealer"]["total"] > 21:
            print("You win!")
        elif card_on_hands["player"]["total"] == card_on_hands["dealer"]["total"]:
            print("It's a draw!")
        else:
            print("You lose!")

        if sum(len(cards) for cards in suits.values()) < 6:
            print("Deck will be refreshed on the next deal.")
            cards_reset()

    elif play_game == 'n':
        print("Game over!")
        play_blackjack = False
    else:
        print("Please input 'y' for yes or 'n' for no only.")