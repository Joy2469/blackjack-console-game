# Aditi Jain
# Blackjack game
# For displaying cards UTF-8 linux based symbols are used

# for installing shuffle

import random


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


# TEST CASES
test_card_1 = Card('Diamonds', '4')
test_card_2 = Card('Clubs', 'Ace')
test_card_3 = Card('Spades', 'Jack')
test_card_4 = Card('Hearts', '10')

# print(ascii_version_of_card(test_card_1, test_card_2, test_card_3, test_card_4))
# print(ascii_version_of_hidden_card(test_card_1, test_card_2, test_card_3, test_card_4))
# # print(ascii_version_of_hidden_card(test_card_1, test_card_2))

# Creating a deck of cards
cards = [
    Card('Diamonds', '2'), Card('Diamonds', '3'), Card('Diamonds', '4'), Card('Diamonds', '5'), Card('Diamonds', '6'),
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

# shuffling the list
random.shuffle(cards)

# Creating empty list for dealer and player
dealer = []
player = []

# no of cards distributed
global distributed_card_no
distributed_card_no = 0


# appends one items at the end of the list
def add_card_player(distributed_card_no):
    player.append(cards[distributed_card_no])
    distributed_card_no = distributed_card_no + 1


def add_card_dealer(distributed_card_no):
    dealer.append(cards[distributed_card_no])
    distributed_card_no = distributed_card_no + 1

player.append(cards[distributed_card_no])# player gets first card
dealer.append(cards[distributed_card_no ]) # dealer gets first card
player.append(cards[distributed_card_no ]) # player gets 2nd card
dealer.append(cards[distributed_card_no]) # dealer gets 2nd card

# player and dealer each have two cards
for i in player:
    print(ascii_version_of_card(player.))
# print(ascii_version_of_hidden_card(dealer))
