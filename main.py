import random
from modulo2 import logo

def dealer_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
        return 'you went over. You lose'

    if user_score == computer_score:
        return 'Draw'
    elif user_score == 0:
        return 'you have a blackjack '
    elif computer_score == 0:
        return 'computer have a blackjack'
    elif computer_score > 21:
        return 'the computer went over. you win'
    elif user_score > 21:
        return 'you went over. you lose'
    elif user_score > computer_score:
        return 'you win'
    else:
        return 'you lose'
        
def play_game():
    print(logo)


    user_cards = []
    computer_cards = []
    is_game_over = False


# Reparte dos cartas 
    for _ in range(2):
        user_cards.append(dealer_card())
        computer_cards.append(dealer_card())
# checar si termino el juego 
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'  your card:{user_cards}, current score:{user_score}')
        print(f'  computers first card:{computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            one_card = input('do you want other card?, type "y" or "n"')
        if one_card == 'Y':
            user_cards.append(dealer_card())
        else:
            is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(dealer_card())
        computer_score = calculate_score(computer_cards)
        print(f'you final hand :{user_cards} , final socre:{user_score}')
        print(f' computers final  hand:{computer_cards}, final score:{computer_score}')
        print(compare(user_score, computer_score))


while input('do you want to play a game of blackjack?: type "y"  or "n":') == 'y':

 play_game()
