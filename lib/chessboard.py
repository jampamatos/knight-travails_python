class ChessBoard:
    size = None

    def __init__(self, size = 8):
      self.set_size(size)
      self.board = [[{'x': x, 'y': y, 'steps': 0} for x in range(self.size)] for y in range(self.size)]

    def is_valid(self, x, y):
      return (0 <= x < self.size) and (0 <= y < self.size)

    @classmethod
    def set_size(cls, size):
        cls.size = size
