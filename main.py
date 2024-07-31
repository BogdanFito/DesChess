import random

import pygame

from data.classes.Board import Board

pygame.init()

WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

def draw(display):
	display.fill('white')
	board.draw(display)
	pygame.display.update()


if __name__ == '__main__':
	running = True
	while running:
		mx, my = pygame.mouse.get_pos()
		for event in pygame.event.get():
			# Quit the game if the user presses the close button
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN and board.turn == 'white':
       			# If the mouse is clicked
				if event.button == 1:
					board.handle_click(mx, my)
		if board.turn == 'black' and not board.is_in_checkmate('black'):
			pieces = []
			for i in range(8):
				for j in range(8):
					piece = board.get_piece_from_pos((i,j))
					if piece is not None and piece.color == 'black' and len(piece.get_valid_moves(board))>0:
						pieces.append(piece)
			piece = pieces[random.randint(0, len(pieces)-1)]
			piece.move(board, piece.get_valid_moves(board)[random.randint(0, len(piece.get_valid_moves(board))-1)])
			board.turn = 'white'

		if board.is_in_checkmate('black'): # If black is in checkmate
			print('White wins!')
			running = False
		elif board.is_in_checkmate('white'): # If white is in checkmate
			print('Black wins!')
			running = False
		# Draw the board
		draw(screen)