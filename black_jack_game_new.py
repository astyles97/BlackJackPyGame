from operator import not_
import sys
import art 
import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card 

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) ==21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, npc_score):
    if player_score > 21:
        if npc_score > 21 and player_score > 21:
            return "You went over, you lost."
        return "You went over, you lost."
    elif player_score == npc_score:
        return "It's a draw."
    elif npc_score < player_score <= 21:
        return "Congratulations, you win!"
    elif player_score < npc_score <= 21:
        return "Opponent won, you lost."
    elif player_score == 0:
        return "Black Jack, you won!"
    elif npc_score == 0:
        return "Terrible luck! Your opponent has a Black Jack, you lost."


def play_game():

    print(art.logo)

    player_cards = []
    npc_cards = []
    is_game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        npc_cards.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_cards)
        npc_score = calculate_score(npc_cards)
        print(f"Your cards: {player_cards} Current score: {player_score}")
        print(f"Computer's first card: {npc_cards[0]}")

        if player_score == 0 or npc_score == 0:
            is_game_over = True
        else:
            should_deal = input("Would you like another card? Type 'y' for yes, 'n' for no.")
            if should_deal == 'y':
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while npc_score != 0 and npc_score < 17:
        npc_cards.append(deal_card())
        npc_score = calculate_score(npc_cards)

    print(f"Your Cards: {player_cards} Your Final Score: {player_score}")
    print(f"Computer's cards: {npc_cards} Computer's Final Score: {npc_score}")
    print(compare(player_score, npc_score))

    while input("Would you like to play a game of Black Jack? Type 'y' for yes, 'n' for no.") == 'y':
        play_game()

play_game()


    
