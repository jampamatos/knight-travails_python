from chessboard import ChessBoard

class Square:
  def __init__(self, x, y, steps):
    self.x = x
    self.y = y
    self.steps = steps

  def is_valid(self):
    return (0 <= self.x < ChessBoard.size) and (0 <= self.y < ChessBoard.size)