import random
def black_jack_game():
    answer = input("Do you want to play blackjack? ('y') or ('n'):\n").lower()
    if answer == 'y':

        play_again = 'y'
        while play_again == 'y':

            # list of cards
            cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

            # Getting two cards

            # Computer
            computer_cards = []
            for i in range(1,3):
                random_card = random.choice(cards)
                computer_cards.append(random_card)
                cards.remove(random_card)
                if 11 in computer_cards and 10 in computer_cards:
                    print(f"Computer's cards are {computer_cards} current score is {sum(computer_cards)}. COMPUTER WINS")
            else:
                print(f"The first computer's card is {computer_cards[0]}")

            your_cards = []
            for i in range(1,3):
                random_card = random.choice(cards)
                your_cards.append(random_card)
                cards.remove(random_card)

            # Your cards
            if 11 in your_cards and 10 in your_cards:
                print(f"Your cards are {your_cards} current score is {sum(your_cards)}. YOU WIN")
            else:
                print(f"Your cards are {your_cards} current score is {sum(your_cards)}")

            sum_of_your_cards = sum(your_cards)

            while sum_of_your_cards < 21:

                your_turn = input("Do you want to hit ('h') or do you want to stand ('s')? ")

                if your_turn == 'h':
                    # Computer's turns
                    if len(your_cards) > 4:
                        random_card = random.choice(cards)
                        computer_cards.append(random_card)
                        cards.remove(random_card)

                    random_card = random.choice(cards)
                    if random_card == 11 and len(your_cards) > 3:
                        random_card = 1
                        your_cards.append(random_card)
                        cards.remove(random_card)
                        print(f"Your cards are {your_cards} current score is {sum(your_cards)}")
                        sum_of_your_cards = sum(your_cards)
                    else:
                        # Replace 11 by 1 if you have more cards
                        if 11 in your_cards:
                            your_cards.remove(11)
                            your_cards.append(1)
                        your_cards.append(random_card)
                        cards.remove(random_card)

                        print(f"Your cards are {your_cards} current score is {sum(your_cards)}")
                        sum_of_your_cards = sum(your_cards)
                else:
                    break

            # Conclusion
            sum_of_computer_cards = sum(computer_cards)
            print(f"Your final cards are {your_cards}, and your current score is {sum_of_your_cards}")

            print(f"The computer's final cards are {computer_cards} it's current score is {sum_of_computer_cards}")

            # Comparing scores
            if sum_of_your_cards == 21 and sum_of_computer_cards == 21:
                print("It's a draw")
            elif sum_of_your_cards == 21:
                print("You win")
            elif sum_of_computer_cards == 21:
                print("Computers wins")
            elif sum_of_your_cards < 21 and sum_of_computer_cards > 21:
                print("You win")
            elif sum_of_computer_cards < 21 and sum_of_your_cards > 21:
                print("Computers wins")
            elif sum_of_your_cards > sum_of_computer_cards:
                print("You win")
            elif sum_of_your_cards < sum_of_computer_cards:
                print("Computers wins")
            elif sum_of_computer_cards == sum_of_your_cards:
                print("It's a draw")

            play_again = input("Do you want to play again?\n").lower()
            if play_again == 'y':
                play_again = 'y'
            else:
                break
    else:
        print("That's ok")

black_jack_game()