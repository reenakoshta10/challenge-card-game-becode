from utils.game import Board


board = Board()
number_of_players = input("How many players wants to play game:")

while number_of_players.isnumeric() == False:
    number_of_players= input("Please enter a valid number: ")
else:
    number_of_players= int(number_of_players)
board.start_game(number_of_players)
