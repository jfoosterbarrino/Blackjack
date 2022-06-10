# Randomized deck of all 52 cards.

# Give player and dealer 2 cards, but display only the players cards that

# Give player option to 'Hit' and get one additional card as many times as they'd like, display card count everytime

# If player goes over '21' then they 'Bust' and dealer wins, dealer can also bust

# If the player get '21' on the first deal, the player wins and this is referred to as blackjack

# If player is closer to 21 than the dealer after choosing to 'stand' then display dealer's hand and player wins

# If dealer is closer to 21 than the player after choosing to 'stand' then display dealer's hand and dealer wins


import random
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class BlackJack():
    hearts_ace = 1
    hearts_2 = 2
    hearts_3 = 3
    hearts_4 = 4
    hearts_5 = 5
    hearts_6 = 6
    hearts_7 = 7
    hearts_8 = 8
    hearts_9 = 9
    hearts_10 = 10
    hearts_jack = 10
    hearts_queen = 10
    hearts_king = 10
    clubs_ace = 1
    clubs_2 = 2
    clubs_3 = 3
    clubs_4 = 4
    clubs_5 = 5
    clubs_6 = 6
    clubs_7 = 7
    clubs_8 = 8
    clubs_9 = 9
    clubs_10 = 10
    clubs_jack = 10
    clubs_queen = 10
    clubs_king = 10
    diamonds_ace = 1
    diamonds_2 = 2
    diamonds_3 = 3
    diamonds_4 = 4
    diamonds_5 = 5
    diamonds_6 = 6
    diamonds_7 = 7
    diamonds_8 = 8
    diamonds_9 = 9
    diamonds_10 = 10
    diamonds_jack = 10
    diamonds_queen = 10
    diamonds_king = 10
    spades_ace = 1
    spades_2 = 2
    spades_3 = 3
    spades_4 = 4
    spades_5 = 5
    spades_6 = 6
    spades_7 = 7
    spades_8 = 8
    spades_9 = 9
    spades_10 = 10
    spades_jack = 10
    spades_queen = 10
    spades_king = 10


    CARD_DECK = (hearts_ace, hearts_2,hearts_3,hearts_4,hearts_5,hearts_6,hearts_7,hearts_8,hearts_9,hearts_10,hearts_jack,hearts_queen,hearts_king,clubs_ace, clubs_2,clubs_3,clubs_4,clubs_5,clubs_6,clubs_7,clubs_8,clubs_9,clubs_10,clubs_jack,clubs_queen,clubs_king,diamonds_ace, diamonds_2,diamonds_3,diamonds_4,diamonds_5,diamonds_6,diamonds_7,diamonds_8,diamonds_9,diamonds_10,diamonds_jack,diamonds_queen,diamonds_king,spades_ace, spades_2,spades_3,spades_4,spades_5,spades_6,spades_7,spades_8,spades_9,spades_10,spades_jack,spades_queen,spades_king)

    def __init__(self):
        self.card = BlackJack.CARD_DECK[random.randint(0,len(BlackJack.CARD_DECK)-1)]
        self.cards = []
        self.dealer_cards = []
        self.drawn_cards = []

    def play_game(self, player_name):
        self.player_name = player_name
        self.cards.hit()
        self.cards.hit()
        self.dealer_cards.hit()
        self.dealer_cards.hit()
        print(self.cards)
        
        while sum(self.cards) <= 21:
            response = input("Hit[h] or Pass[p]?")
            if response.lower() == "h":
                self.cards.hit()
                print(self.cards)
                break
            elif response.lower() == "p":
                self.check_score()
                break
            else:
                print("Invalid response")
        return "Sorry you busted. You Lose!"

    def hit(self):
        if self.card not in self.drawn_cards:
            self.cards.append(self.card)
            self.drawn_cards.append(self.card)