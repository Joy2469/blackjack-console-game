# Aditi Jain
# Blackjack game
# For displaying cards UTF-8 linux based symbols are used


from os import system, name  # for clearing the screen with the help of os.system
import random  # for installing shuffle


def error_check(statement, typ):
    if typ == "string":
        while True:
            choice = input(statement)
            if choice == 'Y' or choice == 'N':
                return choice
            else:
                print("Error: enter a valid value")

    if typ == 'int':
        while True:
            choice = input(statement)
            if choice == '1' or choice == '2':
                return choice
            else:
                print("Error: enter a valid value")


print("Do you want to play BlackJack ♠♦♥♣ [Y/N]")

while True:

    play = error_check('Your Choice: ', 'string')

    """
    Here we are not checking for string becuse too much input validation in the game will destroy 
    the experience 
    """

    if play == 'Y':
        bet = int(input("\nHow much money do you want to bet (50-1000):"))
        print("")


        # ---------------------------------------------
        # CARDS
        # ---------------------------------------------
        class Card(object):
            card_values = {
                'Ace': 11,  # value of the ace is high until it needs to be low
                '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9,
                '10': 10,
                'Jack': 10,  # Jack, Queen and king have 10 value
                'Queen': 10,
                'King': 10
            }

            # constructor
            def __init__(self, suit, rank):
                """
                suit: e.g. Spade or Diamond
                rank: e.g 3 or King
                """
                self.suit = suit.capitalize()
                self.rank = rank
                self.points = self.card_values[rank]


        CARD = """\
        ┌───────────┐
        │{}         │
        │           │
        │           │
        │     {}    │
        │           │
        │           │
        │         {}│
        └───────────┘
        """.format('{rank: <2}', '{suit: <2}', '{rank: >2}')

        HIDDEN_CARD = """\
        ┌───────────┐
        │░░░░░░░░░░░│
        │░░░░░░░░░░░│
        │░░░░░░░░░░░│
        │░░░░░░░░░░░│
        │░░░░░░░░░░░│
        │░░░░░░░░░░░│
        │░░░░░░░░░░░│
        └───────────┘
        """


        def join_lines(strings):
            """
            Stack strings horizontally.
            This doesn't keep lines aligned unless the preceding lines have the same length.
            :param strings: Strings to stack
            :return: String consisting of the horizontally stacked input
            """
            liness = [string.splitlines() for string in strings]
            return '\n'.join(''.join(lines) for lines in zip(*liness))


        def ascii_version_of_card(*cards):
            """
            Instead of a boring text version of the card we render an ASCII image of the card.
            cards: One or more card objects
            :return: A string, the nice ascii version of cards
            """

            # we will use this to prints the appropriate icons for each card
            name_to_symbol = {
                'Spades': '♠',
                'Diamonds': '♦',
                'Hearts': '♥',
                'Clubs': '♣',
            }

            def card_to_string(card):
                # 10 is the only card with a 2-char rank abbreviation
                rank = card.rank if card.rank == '10' else card.rank[0]

                # add the individual card on a line by line basis
                return CARD.format(rank=rank, suit=name_to_symbol[card.suit])

            return join_lines(map(card_to_string, cards))


        def ascii_version_of_hidden_card(*cards):
            """
            Essentially the dealers method of print ascii cards. This method hides the first card, shows it flipped over
            :param cards: A list of card objects, the first will be hidden
            :return: A string, the nice ascii version of cards
            """

            return join_lines((HIDDEN_CARD, ascii_version_of_card(*cards[1:])))


        # Creating a deck of cards
        cards = [
            Card('Diamonds', '2'), Card('Diamonds', '3'), Card('Diamonds', '4'), Card('Diamonds', '5'),
            Card('Diamonds', '6'),
            Card('Diamonds', '7'), Card('Diamonds', '8'), Card('Diamonds', '9'), Card('Diamonds', '10'),
            Card('Diamonds', 'Jack'), Card('Diamonds', 'Queen'), Card('Diamonds', 'King'), Card('Diamonds', 'Ace'),
            Card('Clubs', '2'), Card('Clubs', '3'), Card('Clubs', '4'), Card('Clubs', '5'), Card('Clubs', '6'),
            Card('Clubs', '7'), Card('Clubs', '8'), Card('Clubs', '9'), Card('Clubs', '10'), Card('Clubs', 'Jack'),
            Card('Clubs', 'Queen'), Card('Clubs', 'King'), Card('Clubs', 'Ace'),
            Card('Spades', '2'), Card('Spades', '3'), Card('Spades', '4'), Card('Spades', '5'), Card('Spades', '6'),
            Card('Spades', '7'), Card('Spades', '8'), Card('Spades', '9'), Card('Spades', '10'), Card('Spades', 'Jack'),
            Card('Spades', 'Queen'), Card('Spades', 'King'), Card('Spades', 'Ace'),
            Card('Hearts', '2'), Card('Hearts', '3'), Card('Hearts', '4'), Card('Hearts', '5'), Card('Hearts', '6'),
            Card('Hearts', '7'), Card('Hearts', '8'), Card('Hearts', '9'), Card('Hearts', '10'), Card('Hearts', 'Jack'),
            Card('Hearts', 'Queen'), Card('Hearts', 'King'), Card('Hearts', 'Ace'),
        ]

        # ---------------------------------------------
        # CARDS ENDS
        # ---------------------------------------------

        # shuffling the list
        random.shuffle(cards)

        # Creating empty list for dealer and player
        dealer = []
        player = []


        def add_card_player():  # appends one items at the end of the list
            player.append(cards.pop())


        def add_card_dealer():
            dealer.append(cards.pop())


        # shuffling to generate the random order
        seed = random.random()
        random.seed(seed)
        random.shuffle(cards)

        add_card_player()
        add_card_dealer()
        add_card_player()
        add_card_dealer()


        def calc_hand(hand):
            sum = 0
            for i in hand:  # calculating the sum of the entire hand assuming A=11
                sum = sum + i.points

            for j in hand:
                if sum > 21 and i.points == 11:
                    sum = sum - 10

            return sum


        # define our clear function
        # we need to de clutter the screen as this is a game and
        # and we want it to be user friendly.
        # we use cls if it is windows  (os name in memeory is 'nt')
        # otherwise(linux) we use clear
        def clear():
            # for windows
            if name == 'nt':
                _ = system('cls')

                # for mac and linux(here, os.name is 'posix')
            else:
                _ = system('clear')


        standing = False
        first_hand = True
        game_end = False

        while True:

            player_score = calc_hand(player)
            dealer_score = calc_hand(dealer)

            clear()

            if standing:
                print('Dealer Cards:', dealer_score)
                print(ascii_version_of_card(*dealer))
            else:
                print('Dealer Cards:')
                print(ascii_version_of_hidden_card(
                    *dealer))  # we are passing it as *dealer as we need to pass the address
            print('\nYour Cards:', player_score)
            print(ascii_version_of_card(*player))

            if player_score > 21:
                print('You busted!')
                print("Money lost: $", bet)
                break

            if first_hand:
                double_down = error_check("Do you want to double-down [Y/N]:", 'string')
                if double_down == 'Y':
                    bet = bet * 2
                    add_card_player()
                    standing = True
                    error_in = False
                    while calc_hand(dealer) <= 16:
                        add_card_dealer()
                    clear()
                    player_score = calc_hand(player)
                    print('\nDealer Cards:', dealer_score)
                    print(ascii_version_of_card(*dealer))
                    print('\nYour Cards:', player_score)
                    print(ascii_version_of_card(*player))

            if player_score > 21:
                print('You busted!')
                print("Money lost: $", bet)
                break

            if standing:
                if dealer_score > 21:
                    print("Dealer busted, you win")
                    print("Money bet: $", bet)
                    print("Money earned: $", bet)
                elif player_score == dealer_score:
                    print("Push, nobody wins or loses")
                    print("No money lost or won")
                    print("Money: ", bet)
                elif player_score > dealer_score:
                    print("You beat the dealer, You Win!!!")
                    print("Money bet: $", bet)
                    print("Money earned: $", bet)
                    print(
                        "────────────────────────────────────────────────────────────────────────────────────────────────────")
                    print(
                        "****************************************************************************************************")
                    print(
                        "────────────────────────────────────────────────────────────────────────────────────────────────────")
                    print(
                        "***     ***      ****       ***      ***          ***                   ***   ***   ******      ***")
                    print(
                        " ***   ***     ***  ***     ***      ***          ***                   ***   ***   *** ***     ***")
                    print(
                        "  *** ***     ***    ***    ***      ***          ***       *****       ***   ***   ***  ***    ***")
                    print(
                        "   *****     ***      ***   ***      ***          ***      *** ***      ***   ***   ***   ***   ***")
                    print(
                        "    ***       ***    ***     ***    ***            ***    ***   ***    ***    ***   ***    ***  ***")
                    print(
                        "    ***        ***  ***       ***  ***              ***  ***     ***  ***     ***   ***     *** ***")
                    print(
                        "    ***          ****          ******                ******       ******      ***   ****     ****** "
                        "                    ")
                    print(
                        "────────────────────────────────────────────────────────────────────────────────────────────────────")
                    print(
                        "****************************************************************************************************")
                    print(
                        "────────────────────────────────────────────────────────────────────────────────────────────────────")

                else:  # dealer score is greater than your but lesser than 22
                    print('You Lose :/')
                    print("Money lost: $", bet)

                break

            if first_hand and player_score == 21:
                if dealer_score == 21:
                    print("Both you and dealer have Blackjack")
                    print("Push, nobody wins or loses")
                    print("No money lost or won")
                    print("Money: ", bet)
                else:
                    # Blackjack gets paid 3 to 2
                    print("BlackJack! Nice!")
                    print("Money bet: $", bet)
                    print("Money earned: $", bet * 3 / 2.0)
                    print(
                        "────────────────────────────────────────────────────────────────────────────────────────────────────")
                    print(
                        "****************************************************************************************************")
                    print(
                        "────────────────────────────────────────────────────────────────────────────────────────────────────")
                    print(
                        "***     ***      ****       ***      ***          ***                   ***   ***   ******      ***")
                    print(
                        " ***   ***     ***  ***     ***      ***          ***                   ***   ***   *** ***     ***")
                    print(
                        "  *** ***     ***    ***    ***      ***          ***       *****       ***   ***   ***  ***    ***")
                    print(
                        "   *****     ***      ***   ***      ***          ***      *** ***      ***   ***   ***   ***   ***")
                    print(
                        "    ***       ***    ***     ***    ***            ***    ***   ***    ***    ***   ***    ***  ***")
                    print(
                        "    ***        ***  ***       ***  ***              ***  ***     ***  ***     ***   ***     *** ***")
                    print(
                        "    ***          ****          ******                ******       ******      ***   ****     ****** "
                        "                    ")
                    print(
                        "────────────────────────────────────────────────────────────────────────────────────────────────────")
                    print(
                        "****************************************************************************************************")
                    print(
                        "────────────────────────────────────────────────────────────────────────────────────────────────────")

                break

            first_hand = False

            # showing the menu
            print("")
            print("What would you like to do?")
            print(" [1] Hit")
            print(" [2] Stand")

            choice = error_check('Your Choice: ', 'int')
            print("\n")

            if choice == '1':  # hit
                add_card_player()

            elif choice == '2':
                """
                 we need to calculate dealers hand
                """
                standing = True
                # handles soft 17. The dealer must draw on 16 and stand on 17
                # here is we have <=16 we will draw a card, otherwise
                # we continue with the while loop where now standing is true and result is revealed
                while calc_hand(dealer) <= 16:
                    add_card_dealer()

        print("\nDo you want To play BlackJack ♠♦♥♣ again [Y/N]?")

    elif play == 'N':
        break
