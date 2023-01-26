from lib.chessboard import ChessBoard
from lib.knight import Knight

chessboard = ChessBoard()
knight = Knight(chessboard)

print(knight.find_valid_moves())
knight.move_to([3,4])
print(knight.find_valid_moves())