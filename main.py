import random
from art import logo

# Function that will return the total sum of the cards for each player hand everytime it is called.
from structure import cards


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
            print(f"Your hand: {user}. Computer's hand: {computer}. You lose.\n")
            return False
        else:
            print(f"Your hand: {user}. Computer's hand: {computer}.You win.\n")
            return True
    elif sum_score(computer) == 21:
        print(f"Your hand: {user}. Computer's hand: {computer}.You lose.\n")
        return False
    else:
        input(f"Your score is {sum_score(user)}. Press 'd' if you want to draw a card, if you want to pass type 'p': ")
        draw_card(user)


# Draw a card for the player
def draw_card(player):
    draw = True
    while draw:
        check_ace(player)

        if sum_score(user) > 21:
            print(f"Your hand: {user}. Computer's hand: {computer}. Your final score is {sum_score(user)}, you lose.")
            draw = False

            # Exit game ---

        elif sum_score(user) == 21:
            # Now computer will draw cards.
            computer_play()
            # Another function will compare here if user's score is higher than computer score
            checker()
            draw = False

        else:
            next_draw = input(f"Your current score is {sum_score(user)}. Press 'd' to draw again, or 'p' to pass: ")
            if next_draw == 'd':
                draw = True
            else:
                print(f"Your hand: {user}. Computer's hand: {computer}. Your final score is {sum_score(user)}.")
                # Now computer will draw cards.
                computer_play()
                # Another function will compare here if user's score is higher than computer score
                checker()
                draw = False


# Check if cards[0] is an Ace, and it counts as 1 or 11 depending on the score.
def check_ace(player):
    new_card = random.choice(cards)

    if player == user:
        if new_card == cards[0]:
            if sum_score(user) <= 10:
                new_card = 11
                player.append(new_card)
                sum_score(player)
            else:
                new_card = 1
                player.append(new_card)
                sum_score(player)
        else:
            player.append(new_card)
            sum_score(player)

    elif player == computer:
        if new_card == cards[0]:
            if sum_score(computer) <= 10:
                new_card = 11
                player.append(new_card)
                sum_score(player)
            else:
                new_card = 1
                player.append(new_card)
                sum_score(player)
        else:
            player.append(new_card)
            sum_score(player)


# This function will check the user's score and compare it with the computer's.
def checker():
    computer_score = sum_score(computer)
    user_score = sum_score(user)
    if user_score == 21:
        if computer_score == 21:
            print(f"Your hand: {user}. Computer's hand: {computer}. Computer score: {computer_score}. "
                  f"Your score: {user_score}. You lose.")
        else:
            print(f"Your hand: {user}. Computer's hand: {computer}. Computer score: {computer_score}. "
                  f"Your score: {user_score}. You win.")
    elif computer_score == 21:
        print(f"Your hand: {user}. Computer's hand: {computer}. Computer score: {computer_score}. "
              f"Your score: {user_score}. You lose.")
    elif computer_score > user_score:
        print(f"Your hand: {user}. Computer's hand: {computer}. Computer score: {computer_score}. "
              f"Your score: {user_score}. You lose.")
    elif computer_score == user_score:
        print(f"Your hand: {user}. Computer's hand: {computer}. Computer score: {computer_score}. "
              f"Your score: {user_score}. It's a draw.")
    else:
        print(f"Your hand: {user}. Computer's hand: {computer}. Computer score: {computer_score}. "
              f"Your score: {user_score}. You win.")
    return False


# Function that will draw cards until their score goes over 16.
def computer_play():
    computer_score = sum_score(computer)
    while computer_score < 16:
        draw_card(computer)
        computer_score = sum_score(computer)
        #checker


# Function that asks the user if they would like to play again.
def play_again():
    if not checker():
        print('Game over. Would you like to play again?')


if __name__ == '__main__':
    print(logo)
    user = [9, 1]
    computer = [1, 10]
    # user = random.sample(cards, 2)
    # computer = random.sample(cards, 2)

    # print(user)
    # print(computer)
    print(sum_score(user))
    print(sum_score(computer))
    first_computer_card(computer)
    initial_check()

    #draw_card()
