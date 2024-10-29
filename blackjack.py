import random

import art

def card_deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


player = []
computer = []
win_or_lose = ""
plays_game = False

def blackjack():
    print(art.logo)
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if want_to_play == "y":
        plays_game = True
        player.clear()
        computer.clear()
        player_score = 0
        computer_score = 0
    else:
        plays_game = False

    while plays_game:
        for hand in range(2):
            player.append(card_deal())
            computer.append(card_deal())
        player_score = sum(player)
        computer_score = sum(computer)
        print(f"Your cards: {player}, current score: {player_score}")
        print(f"One of the computer's cards: {computer[0]}")
        plays_game = False

    while player_score < 21:
        draw_more_cards = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw_more_cards == "y":
            player.append(card_deal())
            player_score = sum(player)

        while computer_score < 17:
            computer.append(card_deal())
            computer_score = sum(computer)
        print(f"Your final cards: {player}, final score: {player_score}")
        print(f"Computer's final cards: {computer}, computer final score: {computer_score}")
        print(check_winner(player, player_score, computer_score))
        play_again = input("Type 'y' to play again: ")
        if play_again == "y":
            blackjack()
        else:
            break



def check_winner(player, player_score, computer_score):
    if computer_score > 21:
        win_or_lose = "You Win, Dealer Bust!"
    elif player_score > computer_score:
        win_or_lose = "You Win!"
    elif player_score == computer_score:
        win_or_lose = "It's a Draw"
        if player_score == 21:
            if computer_score == 21:
                win_or_lose = "You lose!"
            else:
                win_or_lose = "You win!"
    else:
        win_or_lose = "You Lose!"
    if player_score > 21:
        for hand in range(2):
            if player[hand] == 11:
                player[hand] = 1
            else:
                win_or_lose = "You Bust!"
    return win_or_lose
    return f"Your final cards: {player}, final score: {player_score}"
    return f"Computer's final cards: {computer}, computer final score: {computer_score}"

blackjack()

