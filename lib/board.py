from chessboard_display import ChessBoardDisplay
from knight import Knight

class Board:
  """
  The Board class represents a chess board, with 8x8 dimensions.
  It includes the ChessBoardDisplay class for displaying the board.
  It has two attributes, dimentions which is a 2D list of 8x8 and knight 
  which is an instance of the Knight class.
  """
  def __init__(self):
    self.dimensions = [[0 for _ in range(8)] for _ in range(8)]
    self.knight = Knight()
  
  def move_knight_to(self, position):
    """
    Move the knight to a given position.

    Args:
        position (list): a list of two integers representing the row and 
        column of the desired position
    """
    self.knight.move_to(position)