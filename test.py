import unittest
from chessboard import ChessBoard

class TestChessBoard(unittest.TestCase):
    def setUp(self):
        self.chessboard = ChessBoard()

    def test_is_valid(self):
        self.log('Running test case: x and y < size')
        self.assertTrue(self.chessboard.is_valid(2, 3))
        self.log('Running test case: x and y == size')
        self.assertFalse(self.chessboard.is_valid(8, 8))
        self.log('Running test case: x, y and steps with negative numbers')
        self.assertFalse(self.chessboard.is_valid(-1, -1))
        self.log('Running test case: x and y == size - 1')
        self.assertTrue(self.chessboard.is_valid(7, 7))
        self.log('Running test case: x and y == 0')
        self.assertTrue(self.chessboard.is_valid(0, 0))
        self.log('Running test case: steps != 0')
        self.assertTrue(self.chessboard.is_valid(2, 3))

    def log(self, message):
        print(f'{message}')

if __name__ == '__main__':
    unittest.main()
