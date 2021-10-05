from operator import attrgetter

from utils.card import Card
from utils.player import Deck
from utils.player import Player


class Board:
    """This class will contains the board where the game been played, It has information about the players"""

    def __init__(self):
        self.players: list(
            Player
        ) = []  # It will contain all the players that are playing
        self.turn_count: int = 0
        self.active_cards: Card = []  # It will contain the last card played by each player
        self.history_cards: list(
            Card
        ) = []  # It will contain all the cards played since the start of the game, except for active_cards

    def start_game(self, number_of_player: int):
        """This method will do the following operations:-
        1. Start the game,
        2. Fill a Deck,
        3. Distribute the cards of the Deck to the players.
        4. Make each Player play() a Card, where each player should only play 1 card per turn, 
           and all players have to play at each turn until they have no cards left.
        5. At the end of each turn, print:
          - The turn count.
          - The list of active cards.
          - The number of cards in the history_cards."""
        deck = Deck()
        deck.fill_deck()  # This will fill the deck
        deck.shuffle()  # This will shuffle cards in deck
        for i in range(number_of_player):
            player = Player(input("Enter name of Player "+str(i+1)+" : "))
            self.players.append(player)

        deck.distribute(self.players)  # This will distribute cards to all the players

        player_with_no_card = 0

        # Game will start here
        while player_with_no_card < len(self.players):
            print(
                "\n====================================================================="
            )

            self.turn_count += 1
            for player in self.players:
                played_card = player.play()
                if played_card is not None:
                    # Active card length can be equal to number of player so in every turn
                    # if number of active card is equal to number of players then before adding
                    # new card to active card we me 1st active card to history cards list.
                    if len(self.active_cards) >= len(self.players):
                        self.history_cards.append(self.active_cards[0])
                        self.active_cards.pop(0)
                    self.active_cards.append(played_card)
                else:
                    player_with_no_card += 1

            # Game over when no played left with card
            if player_with_no_card >= len(self.players):
                break

            # find the max value card
            max_card = None
            for card in self.active_cards:
                if max_card is None or max_card.rank > card.rank:
                    max_card = card
                elif max_card.rank == card.rank:
                    if max_card.icon_rank > card.icon_rank:
                        max_card = card

            # Add point to the player played high value card
            self.players[self.active_cards.index(max_card)].points += 1

            # Printing result after each turn
            print("\nTurn count is", self.turn_count)
            print("\nActive cards are:")
            for card in self.active_cards:
                print(card)
            print("The number of cards in the history_cards", len(self.history_cards))

        # find player with highest points
        max_point = max(self.players, key=attrgetter("points")).points
        winners = [p for p in self.players if p.points == max_point]

        # declare the winner of the game
        if(len(winners)>1):
            print("\tIt's a tie")
            print("\tWinners are ", end="")
            message = ' and '.join([winner.name for winner in winners])
            print(message)
        else:
            print("\t", winners[0].name, "is the winner\t")
        print("=====================================================================")

    def __str__(self) -> str:
        message = ""
        message += "\nNumber of players: " + str(len(self.players))
        message += "\nCurrent turn: " + str(self.turn_count)
        message += "\nActive cards are:"
        for card in self.active_cards:
            message += "\n" + str(card)
        message += "\nNumber of cards in history:" + str(len(self.history_cards))
        return message
