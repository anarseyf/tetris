from functools import reduce

class Piece:

  def __init__(self, dots = [(0, 0)]):
    self.dots = dots
    self.rotation = 0

  def rotate(self, clockwise = True):
    self.rotation += 1
    if self.rotation == 4:
      self.rotation = 0
    print("Rotated: " + str(self.rotation))

  def print(self):
    print(self.dots)
    
    
class Board:
  
  def __init__(self, rows=4, cols=5):
    if rows < 1 or cols < 1:
      raise BaseException("Bad args to Board init")
    m = []
    for _ in range(rows):
      m.append([0] * cols)
    self.m = m
    
  def print(self):
    for row in self.m:
      s = "".join(map(lambda c: str(c) + " ", row))
      print(s)

  def isInBounds(self, r: int, c: int) -> bool:
    return r >= 0 and c >= 0 and r < len(self.m) and c < len(self.m[0]) 

  def isAvailable(self, r: int, c: int) -> bool:
    return self.isInBounds(r, c) and self.m[r][c] == 0

  def place(self, piece: Piece, r: int, c: int) -> bool:
    def offset(dot):
      rDot, cDot = dot
      return (r + rDot, c + cDot)

    offsetDots = list(map(offset, piece.dots))

    canFit = reduce(lambda acc, dot: acc and self.isAvailable(*dot), offsetDots)
    if (not canFit):
      return False
    
    for r, c in offsetDots:
      self.m[r][c] = 1

    return True
