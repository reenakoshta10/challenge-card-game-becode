from utils.game import Board


board = Board()
number_of_players = int(input("How many players wants to play game:"))
board.start_game(number_of_players)
