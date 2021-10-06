from utils.game import Board


board = Board()
number_of_players = input("How many players wants to play game:")

# Condition to check weather user entered valid number of players or not
# if number_of_players in not valid it will keep on asking for the valid
# number until user enter the correct one.

while number_of_players.isnumeric() == False:
    number_of_players = input("Please enter a valid number: ")
else:
    number_of_players = int(number_of_players)

# Start the game
board.start_game(number_of_players)
