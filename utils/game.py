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
            player = Player("player" + str(i + 1))
            self.players.append(player)

        deck.distribute(self.players)  # This will distribute cards to all the players
        # Game will start here
        while True:
            print("----------------------------------------------------------")
            self.history_cards.extend(
                self.active_cards
            )  # Adding active cards to history
            self.active_cards.clear()
            self.turn_count += 1

            for player in self.players:
                played_card = player.play()
                if played_card is not None:
                    self.active_cards.append(played_card)

            # Printing result after each turn
            if len(self.active_cards) != 0:
                print("Turn count is", self.turn_count)
                print("Active cards are:")

                for card in self.active_cards:
                    print(card)

                print(
                    "The number of cards in the history_cards", len(self.history_cards)
                )

            if len(self.active_cards) < len(self.players):
                break

    def __str__(self) -> str:
        message = ""
        message += "\nNumber of players: " + str(len(self.players))
        message += "\nCurrent turn: " + str(self.turn_count)
        message += "\nActive cards are:"
        for card in self.active_cards:
            message += "\n" + str(card)
        message += "\nNumber of cards in history:" + str(len(self.history_cards))
        return message
