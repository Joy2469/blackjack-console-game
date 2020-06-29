# Aditi Jain
# Blackjack game
# For displaying cards UTF-8 linux based symbols are used


from os import system, name  # for clearing the screen with the help of os.system
import random  # for installing shuffle

print("Do you want to play BlackJack ♠♦♥♣ [Y/N]")

while True:

    play = input('Your Choice: ')
    print(" ")

    if play == 'Y':
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

        # no of cards distributed
        global distributed_card_no
        distributed_card_no = 0


        # appends one items at the end of the list
        def add_card_player():
            player.append(cards.pop())


        def add_card_dealer():
            dealer.append(cards.pop())


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
        error_in = False
        game_end = False

        while True:

            player_score = calc_hand(player)
            dealer_score = calc_hand(dealer)

            if not error_in:

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

                if standing:
                    if dealer_score > 21:
                        print("Dealer busted, you win")
                    elif player_score == dealer_score:
                        print("Push, nobody wins or loses")
                    elif player_score > dealer_score:
                        print("You beat the dealer, You Win!!!")
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

                    game_end = True

                if first_hand and player_score == 21:
                    print("BlackJack! Nice!")
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

                    game_end = True

                if player_score > 21:
                    print('You busted!')
                    game_end = True

                first_hand = False

            if not game_end:

                # showing the menu
                print("\n")
                print("What would you like to do?")
                print(" [1] Hit")
                print(" [2] Stand")

                print("\n")
                choice = input('Your Choice: ')
                print("\n")

                if choice == '1':  # hit
                    add_card_player()
                    error_in = False

                elif choice == '2':
                    """
                    we need to calculate dealers hand
                    """
                    standing = True
                    error_in = False
                    while calc_hand(dealer) <= 16:
                        add_card_dealer()
                else:
                    print("Error: enter a valid value")
                    error_in = True
                    continue

            if game_end:
                print("Do you want To play BlackJack ♠♦♥♣ again [Y/N]?")
                break

    elif play == 'N':
        break
    else:
        print("Error: enter a valid value")
        continue
