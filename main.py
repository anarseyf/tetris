#!/usr/bin/env python3

# import board
# import neopixel
from classes import Board, Piece
from time import sleep
import os, sys
from tkinter import Tk, Tcl, Label, Frame
from threading import Timer

NUM = 8
OFF = (0,0,0)
RED = (8,0,0)
WHITE = (5,5,5)
NUM_PIXELS = 60
# must be 10, 12, 18, or 21
# PIN = board.D12
# pixels = neopixel.NeoPixel(PIN, NUM_PIXELS, brightness=0.9)

root = Tk()

state = {
  'count': 0,
  'row': 0,
  'col': 0,
  'board': None,
  'piece': None,
  'status': [],
  'paused': False
}

def lightsOff():
  pixels.fill(OFF)
  pixels.show()

def lights(serialized):
  
  pixels.fill(OFF)
  for i in range(min(len(serialized), NUM_PIXELS)):
    dot = serialized[i]
    if dot == 'X':
      pixels[i] = RED
    elif dot == '*':
      pixels[i] = WHITE
  pixels.show()

def tick(state = state):
  Timer(1.0, tick).start()
  if state['paused']:
    return

  state['count'] += 1
  generate()
  gravity()
  update()

def goodbye():
  # lightsOff()
  global root
  root.quit()
  os._exit(0)

def gameOver():
  state['status'].append("GAME OVER")
  update()
  goodbye()

def generate(state = state):
  if state['piece']:
    return

  piece = Piece(dots = [(0,0), (0,1), (0,2), (1,0)])
  state['piece'] = piece
  row = 0
  col = 2
  placed = board.place(piece, row, col)
  if not placed:
    gameOver()
  state['row'] = row
  state['col'] = col

def gravity(state = state):
  board, piece, row, col, status = (state['board'], state['piece'], state['row'], state['col'], state['status'])

  if not piece:
    return

  row += 1
  placed = board.place(piece, row, col)
  print("Gravity: placed at ({}, {}) ? {}".format(row, col, placed))
  
  if placed:
    state['row'] = row
  else:
    row -= 1
    frozen = board.place(piece, row, col, True)
    if frozen:
      state['piece'] = None
      status.append("Frozen at ({}, {})".format(row, col))
      generate()
    else:
      # raise BaseException("Could not freeze at ({}, {})".format(row, col))
      status.append("! Could not freeze at ({}, {})".format(row, col))

def clear():
  # pass
  os.system('clear')

def update(state = state):
  clear()
  print("tick:", state['count'])
  board = state['board']
  board.print()
  serialized = board.serialize(2)
  status = state['status']
  for line in status:
    print(line)
  status.clear()
  # lights(serialized)

def key_pressed(event, state = state):
  
  board, piece, row, col, status = (state['board'], state['piece'], state['row'], state['col'], state['status'])
  
  key = event.keysym
  if key.lower() in ['c', 'x', 'q']:
    print("EXITING...")
    goodbye()

  if key.lower() == 'p':
    state['paused'] = not state['paused']
    status.clear()
    status.append("PAUSED" if state['paused'] else "RESUMED")
    update()
    return

  if not piece:
    status.append("Piece is empty")
    update()
    return

  newPiece = Piece(piece.dots)

  if key == "Up":
    newPiece.rotate()
  if key == "Down":
    row += 1
  if key == "Left":
    col -= 1
  if key == "Right":
    col += 1

  coords = (row, col)
  placed = board.place(newPiece, *coords)
  status.append("Placed at ({},{})? {}".format(row, col, placed))

  if placed:
    state['row'] = row # TODO - row/col belong to Piece
    state['col'] = col
    state['piece'] = newPiece

  update()

ROWS = 6
COLS = 8
board = Board(ROWS, COLS)
state['board'] = board

tick()

root.bind("<Key>", key_pressed)
frame = Frame(root, width=200, height=50)
frame.pack()
frame.focus_set()
root.mainloop()
clear()

