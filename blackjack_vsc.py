import random

def random_card():
    return random.randint(1, 13)

def card_values(card, hand_value):
    if card >= 10:
        return 10
    if card == 1:
        if hand_value + 11 <= 21:
            return 11
        elif hand_value + 11 >= 21:
            return 1
    else:
        return card

def main():
    player_hand = 0
    dealer_hand = 0

    print("Let's Play Blackjack\n")
    while True:
        player_card = random_card()
        dealer_card = random_card()

        player_hand += card_values(player_card, player_hand)
        dealer_hand += card_values(dealer_card, dealer_hand)

        print(f"Your card is {player_card}. Your total hand is {player_hand}\n")
        print(f"Dealer's card is {dealer_card}. Dealer's total hand is {dealer_hand}\n")

        if player_hand == 21:
            print("Blackjack! You win!")
            break
        if player_hand > 21:
            print("Bust! You lose!")
            break

        choice = input("Do you (H)it or (S)tand? ").strip()

        if choice == 's' or choice == 'S':
            while dealer_hand < 17:
                dealer_card = random_card()
                dealer_hand += card_values(dealer_card, dealer_hand)
                print(f"Dealer's final card is {dealer_card}. Dealer's total hand is {dealer_hand}.\n")

            if dealer_hand > 21 or dealer_hand < player_hand:
                print("You win!")
            elif dealer_hand > player_hand:
                print("Dealer wins.")
            else:
                print("It's a tie!")
            break

    print("Thank you for playing!")

if __name__ == "__main__":
    main()
