class ChessBoardDisplay:

  """
  This class is responsible for displaying the chess board and the knight's position in it.
  """
  def display(self, board):
    """
    Prints all the cells in the chess board on the console, along with the letters and numbers for coordenates.

    Args:
        board (object): an instance of the board class that contains all board's information.
    """
    print('   A  B  C  D  E  F  G  H')
    for x in range(8):
      print(f"{x+1} ", end='')
      for y in range(8):
        self._print_cell(x, y, board)
      print()
  
  def _print_cell(self, x, y, board):
    """
    Print each individual cells of the board, along with the knight, when in position.

    Args:
        x (int): row index of the cell
        y (int): column index of the cell
        board (object): an instance of the board class that contains all board's information.
    """
    if board.knight.knight_position[0] == x and board.knight.knight_position[1] == y:
      print(' ♞ ', end='')
    elif (x + y) % 2 == 0:
      print('⬜ ', end='')
    else:
      print('⬛ ', end='')
  
