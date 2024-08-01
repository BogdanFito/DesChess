import random
import chess
import pygame

from data.classes.Board import Board

pygame.init()

WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])
board2 = chess.Board()

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
				if event.button == 1:
					m = board.handle_click(mx, my)
					if m is not None:
						board2.push_san(m)
						print(m)

		if board.turn == 'black' and not board2.is_checkmate():
			pieces = []
			for i in range(8):
				for j in range(8):
					piece = board.get_piece_from_pos((i,j))
					if piece is not None and piece.color == 'black' and len(piece.get_valid_moves(board))>0:
						pieces.append(piece)
			piece = pieces[random.randint(0, len(pieces)-1)]
			m = piece.get_valid_moves(board)[random.randint(0, len(piece.get_valid_moves(board))-1)]
			piece.move(board, m)
			board2.push_san(piece.getID()+m.get_coord())
			print(piece.getID()+m.get_coord())
			board.turn = 'white'

		if board2.is_checkmate():
			print('Game over')
			running = False
		# Draw the board
		draw(screen)