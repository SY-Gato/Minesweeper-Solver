import numpy as np
import time

boardWidth = 10
boardHeight = 10
mineCount = 1

class Cell: # Values: 0=Unopened, 9=Blank(Opened with no number), 1=1, 2=2, etc
  def __init__(self, isFlagged: bool, Value: int, Row: int, Column: int):
    self.flagged = isFlagged
    self.val = Value
    self.row = Row
    self.col = Column

cells = [

for y in range(0,boardHeight):
  for x in range(0,boardWidth):
    cells[i] = Cell(false, 0

print(list(cells))
