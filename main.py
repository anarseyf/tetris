#!/usr/bin/env python3

from board import Board, Piece
from time import sleep
from os import system
from tkinter import Tk, Tcl, Label, Frame
from threading import Timer
root = Tk()

state = {
  'count': 0,
  'row': 0,
  'col': 0,
  'board': None,
  'piece': None
}

# def tick():
#     print("tick:", obj['count'])
#     Timer(1.0, tick).start()

def key_pressed(event, state = state):
  
  system('clear')

  board, piece, row, col = (state['board'], state['piece'], state['row'], state['col'])
  
  key = event.keysym
  print("Pressed: " + event.keysym)
  if key == "Up":
    row -= 1
  if key == "Down":
    row += 1
  if key == "Left":
    col -= 1
  if key == "Right":
    col += 1

  coords = (row, col)
  print("New coords: " + str(coords))

  placed = board.place(piece, *coords)
  board.print()
  print("Placed at ({},{})? {}".format(row, col, placed))

  if placed:
    state['row'] = row
    state['col'] = col
# tick()


ROWS = 10
COLS = 10
board = Board(ROWS, COLS)
state['board'] = board
board.print()

piece = Piece(dots = [(0,0), (0,1), (0,2)])
state['piece'] = piece

# row = 1
# col = COLS - 1
# placed = board.place(piece, row, col)
# board.print()
# print("Placed at ({},{})? {}".format(row, col, placed))
# sleep(2)


root.bind("<Key>", key_pressed)
frame = Frame(root, width=0, height=0)
frame.pack()
frame.focus_set()
root.mainloop()
