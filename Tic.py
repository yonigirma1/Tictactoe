#Welcome to TIC TAC TOE game

from __future__ import print_function    						#  import the print function for python 3

import os   													# import operating system for the clear funciton

clear = lambda: os.system('clear')								# clear the screen


# This function prints the board for Tic Tc Toe game
def display_board(board):
	clear()
	print('  |  |')
	print(''+board[7]+ ' | '+board[8]+'| '+board[9])
	print('  |  |')
	print('-----------------')
	print('  |  |')
	print(''+board[4]+ ' | '+board[5]+'| '+board[6])
	print('  |  |')
	print('-----------------')
	print('  |  |')
	print(''+board[1]+ ' | '+board[2]+'| '+board[3])
	print('  |  |')


# This function differrentiate the marker as 'X' or 'O'
def player_input():
	marker = ''
	while not (marker == 'O' or marker == 'X'):
		marker = raw_input("player 1: please enter 'X' or 'O:").upper()
		if marker == 'X':
			return ('X','O')
		else:
			return ('O','X')


#This function places the given marker on the board
def place_marker(board, marker, position):
	board[position] = marker

#chooses who go first
import random
def choose_first():
	if random.randint(0,1) == 0:
		return 'Player 2'
	else:
		return 'Player 1'

#checks if a player wins
def win_check(board, mark):
	return((board[7] == mark and board[8] == mark and board[9] == mark)or
		   (board[4] == mark and board[5] == mark and board[6] == mark) or
		   (board[1] == mark and board[2] == mark and board[3] == mark) or
		   (board[7] == mark and board[4] == mark and board[1] == mark) or
		   (board[8] == mark and board[5] == mark and board[2] == mark) or
		   (board[9] == mark and board[6] == mark and board[3] == mark) or
		   (board[7] == mark and board[5] == mark and board[3] == mark) or
		   (board[9] == mark and board[5] == makr and board[1] == makr)
		)

#checks if there is an available space
def space_check(board, position):
	return board[position] == ' '

#checks if the board is full
def full_board_check(board):
	for i in range(1,10):
		if space_check(board, i):
			return False
		return True
		
#give a player to choice a position
def player_choice(board):
	position = ' '
	while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
		position = raw_input("choose your next move: (0-9): ")
	return int(position)

# provides if players want to rematch	
def replay():
	return raw_input('Do you want to play again? Enter Yes or No').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
	board = [' '] * 10
	player1_marker, player2_marker = player_input()
	turn  = choose_first()
	print(turn+' will go first.')
	game_on = True

	while game_on:
		if turn == 'Player 1':
			display_board(board)
			position = player_choice(board)
			place_marker(board, position, player1_marker)

			if win_check(board, player1_marker):
				display_board(board)
				print('Congradulations, you have won the game')
				game_on = False
			else:
				if full_board_check(board):
					display_board(board)
					print("It is a tie")
					break
				else:
					turn = 'Player 2'

		else:
			display_board(board)
			position = player_choice(board)
			place_marker(board, player2_marker,position)	

			if win_check(board, player2_marker):
				display_board(board)
				print('congradulations, you have won the game')
				game_on = False
			else:
				if full_board_check(board):
					display_board(board)
					print('It is a tie')
					break
				else:
					turn = 'player 1'

	if not replay():
		break										











