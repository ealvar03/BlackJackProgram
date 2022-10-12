import random

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#computer = random.sample(cards, 2)
#user = random.sample(cards, 2)
#computer = [10, 10]
#user = [1, 10]


# user = random.sample(cards, 2)

# Function that will return the total sum of the cards for each player hand everytime it is called.
def sum_score(player_hand):
    initial_score = 0
    for card in player_hand:
        initial_score += card
    return initial_score


# Reveal the computer's first card to the user.
def first_computer_card(computer_input):
    initial_cards = [computer_input[0], "X"]
    print(f"The initial cards for computer are: {initial_cards}")


# Function that will check the initial score at the beginning of the game when the user and the computer
# have two initial cards.
def initial_check():
    if sum_score(user) == 21:
        if sum_score(computer) == 21:
            print("You lose.")
            return False
        else:
            print("You win.")
            return True
    elif sum_score(computer) == 21:
        print("You lose.")
        return False
    else:
        continue_playing = input(f"Your score is {sum_score(user)}. Tap 'd' to draw a card to continue playing, "
                                 f"or 'p' to pass: ")
        if continue_playing == 'd':
            draw_card(user)
        else:
            checker()

# Draw a card for the player
def draw_card(player):
    draw = True
    while draw:
        new_card = random.choice(cards)
        player.append(new_card)
        actual_score = sum_score(player)

        # Checkear por que el valor new_card no funciona
        if new_card == cards[0]:
            if actual_score <= 10:
                new_card = 11
            else:
                new_card = 1

        # When player == user
        if actual_score > 21:
            draw = False
            print(f"Your final score is {actual_score}, you lose.")
            # Exit game ---
        elif actual_score == 21:
            if initial_check():
                draw = False
        else:
            next_draw = input(f"Your current score is {actual_score}. Press 'd' to draw again, or 'p' to pass: ")
            if next_draw == 'd':
                draw = True
            else:
                draw = False
                print(f"Your final score is {actual_score}.")
                # Now computer will draw cards.
                computer_play()
                # Another function will compare here if user's score is higher than computer score
                checker()



# This function will check the user's score and compare it with the computer's.
def checker():
    computer_score = sum_score(computer)
    user_score = sum_score(user)
    if user_score == 21:
        if computer_score == 21:
            print(f"Computer score: {computer_score}. Your score: {user_score}. You lose.")
        else:
            print(f"Computer score: {computer_score}. Your score: {user_score}. You win.")
    elif computer_score == 21:
        print(f"Computer score: {computer_score}. Your score: {user_score}. You lose.")
    elif computer_score > user_score:
        print(f"Computer score: {computer_score}. Your score: {user_score}. You lose.")
    elif computer_score == user_score:
        print(f"Computer score: {computer_score}. Your score: {user_score}. It's a draw.")
    else:
        print(f"Computer score: {computer_score}. Your score: {user_score}. You win.")

# Function that will draw cards until their score goes over 16.
def computer_play():
    computer_score = sum_score(computer)
    while computer_score < 16:
        draw_card(computer)
        computer_score = sum_score(computer)
        checker()


