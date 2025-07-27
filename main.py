
import random
import os

Cards = [2,3,4,5,6,7,8,9,"K","Q","J","A"]




# a function to draw cards from the deck
def DrawCard():
    return random.choice(Cards);

def Check_total(deck):
    total = 0
    for card in deck:
        if type(card) == int:
            total += card
        elif card == "K" or card == "Q" or card == "J":
            total += 10;
        else:
            if total > 10:
                total +=1
            else:
                total += 11

    return total

def Check_exceeds_21(user,total):
    if total > 21:
        if user == "player":
            print("Dealer wins!. 😭 your deck exceeds 21")
        else:
            print("You won!. 😎 Dealer's deck exceeds 21")
        return True
    else:
        return False



# a function for the main gameplay
def BlackJack():
    while True:
        global gameplay
        if gameplay:
            player_cards = [DrawCard(), DrawCard()]
            dealer_cards = [DrawCard(), DrawCard()]

            print(f"Your cards are :- {player_cards}" )
            print(f"Dealer's cards are :- {dealer_cards[0]}")

            while True:
                user_input = input("Do you wish to draw another card? ('y' for yes and 'n' for no) : ")

                if user_input == 'y':
                    player_cards.append(DrawCard())
                    player_total = Check_total(player_cards)
                    Game_status = Check_exceeds_21("player", player_total)
                    print(f"Your cards are :- {player_cards}")
                    print(f"Dealer's cards are :- {dealer_cards[0]}")
                    if Game_status:
                        break;
                elif user_input == 'n':
                    Dealer_total = Check_total(dealer_cards)
                    if Dealer_total < 17:
                        dealer_cards.append(DrawCard())
                        Dealer_total = Check_total(dealer_cards)
                        game_status = Check_exceeds_21("dealer", Dealer_total)

                        break;
                else:
                    print("Enter a valid response");

            player_total = Check_total(player_cards)
            dealer_total = Check_total(dealer_cards)
            print(f"Your cards are :- {player_cards}" )
            print(f"Dealer's cards are :- {dealer_cards}")
            if player_total > dealer_total:
                print("You won !!!!! 🥳")
            else:
                print("You lose !!!!! 😔")

            user_input_play_again = input("How about a re-match?? 😏 ('y' for yes and 'n' for no) : ")
            if user_input_play_again == 'n':
                break



while True:
    user_decision_to_play_the_game = input("Do you want to Enter the game? ('y' for yes and 'n' for no) : ")

    if user_decision_to_play_the_game == 'y':
        global gameplay
        gameplay = True;
        break;
    elif user_decision_to_play_the_game == 'n':

        gameplay = False;
        break;
    else:
        print("Enter a valid response");


BlackJack()