from lib.chessboard import ChessBoard
from lib.knight import Knight

chessboard = ChessBoard()
knight = Knight(chessboard, [2, 0])
chessboard.show_board(knight)
knight.move_to([6,1])
chessboard.show_board(knight)