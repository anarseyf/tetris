from functools import reduce
from enum import Enum
from copy import deepcopy

class Spot(Enum):
  FREE = 0,
  TEMP = 1,
  TAKEN = 2

class Piece:

  def __init__(self, dots = [(0, 0)]):
    self.dots = dots
    self.rotation = 0

  def rotate(self):
    def flip(dot):
      r, c = dot
      return (c, r)

    def mult(dot):
      r, c = dot
      return (-r, c)

    dots = list(map(mult, map(flip, self.dots)))

    self.dots = dots

  def print(self):
    print(self.dots)
    
    
class Board:
  
  def __init__(self, rows=4, cols=5):
    if rows < 1 or cols < 1:
      raise BaseException("Bad args to Board init")
    m = []
    for _ in range(rows):
      m.append([Spot.FREE] * cols)
    self.m = m

  def _isInBounds(self, r: int, c: int) -> bool:
    return r >= 0 and c >= 0 and r < len(self.m) and c < len(self.m[0]) 

  def _isAvailable(self, r: int, c: int) -> bool:
    return self._isInBounds(r, c) and self.m[r][c] != Spot.TAKEN

  def _clearRows(self):
    while True:
      deleted = False
      for r in range(len(self.m)):
        row = self.m[r]
        isComplete = reduce(lambda acc, c: acc and c == Spot.TAKEN, row, True)
        if isComplete:
          del self.m[r]
          self.m.insert(0, [Spot.FREE] * len(row))
          deleted = True
      if not deleted:
        break

  def _clearTemp(self):
    for row in self.m:
      for colNum in range(len(row)):
        if row[colNum] == Spot.TEMP:
          row[colNum] = Spot.FREE

  def place(self, piece: Piece, r: int, c: int, freeze=False) -> bool:
    def offset(dot):
      rDot, cDot = dot
      return (r + rDot, c + cDot)

    offsetDots = list(map(offset, piece.dots))

    canFit = reduce(lambda acc, dot: acc and self._isAvailable(*dot), offsetDots, True)
    if (not canFit):
      return False

    self._clearTemp()
    
    spotType = Spot.TAKEN if freeze else Spot.TEMP
    for r, c in offsetDots:
      self.m[r][c] = spotType

    if freeze:
      self._clearRows()

    return True
    
  def print(self):

    def toStr(dot):
      return "(*)" if dot == Spot.TEMP else "[X]" if dot == Spot.TAKEN else " - "

    for row in self.m:
      s = "".join(map(toStr, row))
      print(s)