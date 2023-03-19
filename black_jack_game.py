import sys
import art 
import random

############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
###########################################################

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#setting the hand so the deal() funct can start adding cards one at a time 
player_hand = [random.choice(cards)]
cpu_hand = [random.choice(cards)*2]

should_continue = True 

def game():
        play_bj = input("Would you like to play a game of Black Jack? Type 'y' or 'n'. ")
        if play_bj == 'y':
            print(art.logo)
            deal_cards()
        else:
          should_continue = False    

def deal_cards():
    player_score = sum(player_hand)
    while should_continue:    
        for card in cards:
            player_hand.append(random.choice(cards))
            cpu_hand.append(random.choice(cards))
            return f"Your cards: {player_hand} Current Score : {player_score} \n Computer's first card: {cpu_hand[0]}"
        if player_score < 21:
            hit = input("Would you like to be dealt another card? Type 'y' for yes and 'n' for pass.")
        if hit == 'y':
            deal_cards()
        if hit == 'n':
            calculate_score()
    else:
        calculate_score()
def calculate_score():
    cpu_score = sum(cpu_hand)
    if player_score == 21 and len(player_hand) == 2:
        player_score = 0
        print(f"Your Cards: {player_hand} Final Score: {player_score}")
        print(f"computer's cards: {cpu_hand} Final score ")
        print("Congratulations! You won with a Black Jack!")
    elif cpu_score == 21 and len(cpu_hand) == 2:
        cpu_score = 0
        print(f"Your Cards: {player_hand} Final Score: {player_score}")
        print(f"Computer's cards: {cpu_hand} Final Score: {cpu_score}")
        print("Terrible luck! Oppenent has a Black jack and you lost.")
    elif player_score > 21:
        print(f"Your Cards: {player_hand} Final Score: {player_score}")
        print(f"computer's cards: {cpu_hand} Final score ")
        print("You went over, it's a bust.")

game()
deal_cards()
calculate_score()




    

    
    
        
             



    