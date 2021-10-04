import random
from typing import List
from utils.card import Card


class Player:
    """This class save the Player game status like how many card he has, what card he has played"""

    def __init__(self, name: str):
        self.name: str = name
        self.cards: list(Card) = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history: list(Card) = []

    def play(self):
        """This function will perform following operations:-
        1. randomly pick a Card in cards.
        2. Add the Card to the Player's history.
        3. Print: {PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}.
        4. Return the Card"""
        if len(self.cards) > 0:
            self.turn_count += 1
            random_card = random.choice(self.cards)  # player selecting randon card
            self.cards.remove(
                random_card
            )  # card will be removed from player cards list
            self.history.append(
                random_card
            )  # and will be moved to list of card history
            print(
                "{} {} played: {} {}.".format(
                    self.name, self.turn_count, random_card.value, random_card.icon
                )
            )
            return random_card
        else:
            return None

    def __str__(self) -> str:
        return self.name + " has " + str(len(self.cards)) + " cards."


class Deck:
    """This class will have actuall Deck which has all the cards and oparation related to cards"""

    def __init__(self):
        self.cards: list(Card) = []

    def fill_deck(self):
        """This method will fill cards with a complete card game (an instance of 'A, 2, 
        3, 4, 5, 6, 7, 8, 9, 10, J, Q, K' for each possible symbol [hearts, diamonds, 
        clubs, spades]). Your deck should contain 52 cards at the end"""
        print("I am filling deck")
        symbols = ["♥", "♦", "♣", "♠"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        # iteration for all symbols and value to get all the card combination possible

        for symbol in symbols:
            for value in values:
                if symbol in ["♥", "♦"]:
                    color = "Red"
                else:
                    color = "Black"
                card = Card(color, symbol, value)
                self.cards.append(card)

    def shuffle(self):
        """This method will shuffle all the list of cards"""
        random.shuffle(self.cards)

    def distribute(self, playerList: List[Player]):
        """This method will distribute the cards evenly between all the players passed 
        by the parameter"""
        print("I am distributing cards")
        i = 0
        while len(self.cards) > i:
            for (
                player
            ) in (
                playerList
            ):  # iterating for all the player and assigning one card everytime
                if len(self.cards) > i:
                    player.cards.append(self.cards[i])
                    i += 1

    def __str__(self) -> str:
        message = ""
        for card in self.cards:
            message += card + "\n"
        return message
