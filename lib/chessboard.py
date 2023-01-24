class ChessBoard:
  size = None
  def __init__(self):
    self.set_size(8)
    self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
  
  @classmethod
  def set_size(cls, size):
    cls.size = size