from os import system, name
import random
from art import logo

# Function that will return the total sum of the cards for each player hand everytime it is called.
from structure import cards


# This function will calculate the player's score.
def get_players_score(player_hand):
    initial_score = 0
    for card in player_hand:
        initial_score += card
    return initial_score


# Reveal the computer's first card to the user.
def show_first_computer_card(computer_input):
    initial_cards = [computer_input[0], "X"]
    print(f"The initial cards for computer are: {initial_cards}")


# Function that will check the initial score at the beginning of the game when the user and the computer
# have two initial cards.
def initial_check():
    if get_players_score(user) == 21:
        if get_players_score(computer) == 21:
            print(f"Your hand: {user}. Computer's hand: {computer}. You lose.\n")
            return False
        else:
            print(f"Your hand: {user}. Computer's hand: {computer}.You win.\n")
            return True
    elif get_players_score(computer) == 21:
        print(f"Your hand: {user}. Computer's hand: {computer}.You lose.\n")
        return False
    else:
        input(f"Your score is {get_players_score(user)}. Press 'd' if you want to draw a card, if you want "
              f"to pass type 'p': ")
        draw_card()


# Draw a card for the player
def draw_card():
    return random.choice(cards)


# Check if cards[0] is an Ace, and it counts as 1 or 11 depending on the score.
def check_ace(player):
    new_card = player[len(player) - 1]
    if player == user:
        if new_card == cards[0]:
            if get_players_score(user) - new_card <= 10:
                player[len(player) - 1] = 11
            else:
                player[len(player) - 1] = 1

    elif player == computer:
        if new_card == cards[0]:
            if get_players_score(computer) - new_card <= 10:
                player[len(player) - 1] = 11
            else:
                player[len(player) - 1] = 1


# This function will check the user's score and compare it with the computer's.
def check_players_score():
    keep_playing = True
    user_score = get_players_score(user)
    while keep_playing:
        next_draw = input(f"Your current score is {user_score}. Press 'd' to draw again, or 'p' to"
                          f" pass: ")
        if next_draw == 'd':
            new_draw = draw_card()
            user.append(new_draw)
            check_ace(user)
            user_score = get_players_score(user)
            keep_playing = True
            if user_score > 21:
                keep_playing = False
        else:
            computer_play()
            keep_playing = False
    show_result()
    # if user_score == 21:
    #     if computer_score == 21:
    #         print(f"Computer's hand: {computer}. Your hand: {user}. Computer score: {computer_score}. "
    #               f"Your score: {user_score}. You lose.")
    #     else:
    #         print(f"Computer's hand: {computer}. Your hand: {user}. Computer score: {computer_score}. "
    #               f"Your score: {user_score}. You win.")
    # elif computer_score == 21:
    #     print(f"Computer's hand: {computer}. Your hand: {user}. Computer score: {computer_score}. "
    #           f"Your score: {user_score}. You lose.")
    # elif computer_score > user_score:
    #     print(f"Computer's hand: {computer}. Your hand: {user}. Computer score: {computer_score}. "
    #           f"Your score: {user_score}. You lose.")
    # elif computer_score == user_score:
    #     print(f"Computer's hand: {computer}. Your hand: {user}. Computer score: {computer_score}. "
    #           f"Your score: {user_score}. It's a draw.")
    # elif user_score > computer_score:
    #     print(f"Computer's hand: {computer}. Your hand: {user}. Computer score: {computer_score}. "
    #           f"Your score: {user_score}. You win.")


# Function that will draw cards until their score goes over 16.
def computer_play():
    computer_score = get_players_score(computer)
    while computer_score < 16:
        new_draw = draw_card()
        computer.append(new_draw)
        check_ace(computer)
        computer_score = get_players_score(computer)


# Function that will show the results and the winner
def show_result():
    computer_score = get_players_score(computer)
    user_score = get_players_score(user)
    if user_score == 21:
        if computer_score == 21:
            print(f"Computer's hand: {computer}. Your hand: {user}. Computer score: {computer_score}. "
                  f"Your score: {user_score}. You lose.")
        else:
            print(f"Computer's hand: {computer}. Your hand: {user}. Computer score: {computer_score}. "
                  f"Your score: {user_score}. You win.")
    elif computer_score == 21:
        print(f"Computer's hand: {computer}. Your hand: {user}. Computer score: {computer_score}. "
              f"Your score: {user_score}. You lose.")
    elif computer_score > user_score:
        if computer_score > 21:
            print(f"Computer's hand: {computer}. Your hand: {user}. Computer score: {computer_score}. "
                  f"Your score: {user_score}. You win.")
        else:
            print(f"Computer's hand: {computer}. Your hand: {user}. Computer score: {computer_score}. "
                  f"Your score: {user_score}. You lose.")
    elif computer_score == user_score:
        print(f"Computer's hand: {computer}. Your hand: {user}. Computer score: {computer_score}. "
              f"Your score: {user_score}. It's a draw.")
    elif user_score > computer_score:
        if user_score > 21:
            print(f"Computer's hand: {computer}. Your hand: {user}. Computer score: {computer_score}. "
                  f"Your score: {user_score}. You lose.")
        else:
            print(f" Computer's hand: {computer}. Your hand: {user}. Computer score: {computer_score}. "
                  f"Your score: {user_score}. You win.")
    play_again()


# To be done: Finish to clear screen
# Function that clears the screen
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')
    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


# Function that asks the user if they would like to play again.
def play_again():
    new_game = input("Press 'y' to play again, press 'n' to leave: ")
    if new_game == 'y':
        clear()
    else:
        print('Goodbye!')


if __name__ == '__main__':
    print(logo)
    user = random.sample(cards, 2)
    computer = random.sample(cards, 2)
    print("Your score: ", get_players_score(user))
    print("Computer's score: ", get_players_score(computer))
    show_first_computer_card(computer)
    check_players_score()



