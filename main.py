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
  'piece': None,
  'status': []
}

def tick(state = state):
  state['count'] += 1
  gravity()
  update()
  Timer(1.0, tick).start()

def gravity(state = state):
  board, piece, row, col, status = (state['board'], state['piece'], state['row'], state['col'], state['status'])

  row += 1
  placed = board.place(piece, row, col)
  print("Gravity: placed at ({}, {}) ? {}".format(row, col, placed))
  
  if placed:
    state['row'] = row
  else:
    row -= 1
    frozen = board.place(piece, row, col, True)
    if frozen:
      status.append("Frozen at ({}, {})".format(row, col))
    else:
      # raise BaseException("Could not freeze at ({}, {})".format(row, col))
      status.append("! Could not freeze at ({}, {})".format(row, col))

def clear():
  # pass
  system('clear')

def update(state = state):
  clear()
  print("tick:", state['count'])
  board = state['board']
  board.print()
  status = state['status']
  for line in status:
    print(line)
  status.clear()

def key_pressed(event, state = state):
  
  board, piece, row, col, status = (state['board'], state['piece'], state['row'], state['col'], state['status'])
  
  key = event.keysym
  if key == "Up":
    row -= 1
  if key == "Down":
    row += 1
  if key == "Left":
    col -= 1
  if key == "Right":
    col += 1

  coords = (row, col)
  status.append("New coords: " + str(coords))

  placed = board.place(piece, *coords)
  status.append("Placed at ({},{})? {}".format(row, col, placed))

  if placed:
    state['row'] = row
    state['col'] = col

  update()

ROWS = 10
COLS = 10
board = Board(ROWS, COLS)
state['board'] = board

piece = Piece(dots = [(0,0), (0,1), (0,2)])
state['piece'] = piece

board.place(piece, 0, 3)

tick()

root.bind("<Key>", key_pressed)
frame = Frame(root, width=0, height=0)
frame.pack()
frame.focus_set()
root.mainloop()
clear()

