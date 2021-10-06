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
        self.points: int = 0

    def play(self):
        """This function will perform following operations:-
        1. randomly pick a Card in cards.
        2. Add the Card to the Player's history.
        3. Print: {PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}.
        4. Return the Card"""
        if len(self.cards) > 0:
            self.turn_count += 1

            # ask player to play a card from the list of card he has.
            print("\n{}, Which card you want to play from below available cards? Please enter the index number."
            .format((self.name).capitalize()))
            print('[', end='')
            for card in self.cards:
                if self.cards.index(card)+1 == len(self.cards):
                    print(self.cards.index(card)+1,' : ', card, end = ']\n')
                else:
                    print(self.cards.index(card)+1,' : ', card, end = ', ')
            selected_card=input()

            # if player selected an invalid card number then it should show the error and ask to select card again.
            #  
            while(selected_card == '' or selected_card.isnumeric() is False 
            or int(selected_card) > len(self.cards) or int(selected_card) < 1):
                selected_card= input("Enter a value number from the list provided: ")
            else:
                selected_card= int(selected_card)

            random_card= self.cards[selected_card-1]
            
            self.cards.remove(
                random_card
            )  # card will be removed from player cards list
            self.history.append(
                random_card
            )  # and will be moved to list of card history
            print(
                "{} {} played: {}.".format(
                    self.name, self.turn_count, random_card
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
        symbols = ["♠", "♥", "♣", "♦"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        # iteration for all symbols and value to get all the card combination possible
        # with card value rank
        icon_rank = 1
        for symbol in symbols:
            rank = 13
            for value in values:
                if symbol in ["♥", "♦"]:
                    color = "Red"
                else:
                    color = "Black"
                card = Card(color, symbol, value, rank, icon_rank)
                rank -= 1
                icon_rank += 1
                self.cards.append(card)

    def shuffle(self):
        """This method will shuffle all the list of cards"""
        random.shuffle(self.cards)

    def distribute(self, playerList: List[Player]):
        """This method will distribute the cards evenly between all the players passed 
        by the parameter"""
        while len(self.cards) > 0:

            # iterating for all the player and assigning one card everytime
            # moving card from deck card to player cards
            for player in playerList:
                player.cards.append(self.cards[0])
                self.cards.pop(0)

            # break execution if cards in deck is less the the number of players
            if len(self.cards) < len(playerList):
                break


    def __str__(self) -> str:
        message = ""
        for card in self.cards:
            message += card + "\n"
        return message
