#!/usr/bin/env python3

from board import Board, Piece

ROWS = 3
COLS = 10
board = Board(ROWS, COLS)
board.print()

piece = Piece(dots = [(0,0), (0,1), (0,2)])
piece.print()
piece.rotate()

row = 1
col = COLS - 1
placed = board.place(piece, row, col)
print("Placed at ({},{})? {}".format(row, col, placed))
board.print()

col = 1
placed = board.place(piece, row, col)
print("Placed at ({},{})? {}".format(row, col, placed))
board.print()

placed = board.place(piece, row, col)
print("Placed at ({},{})? {}".format(row, col, placed))
board.print()