import unittest
import sys
import io

from contextlib import redirect_stdout
from chessboard import ChessBoard
from knight import Knight


class TestChessBoard(unittest.TestCase):
    def setUp(self):
        self.chessboard = ChessBoard()
        self.knight = Knight(self.chessboard, [3, 4])

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


class TestKnight(unittest.TestCase):
    def setUp(self):
        self.chessboard = ChessBoard()
        self.knight = Knight(self.chessboard)

    def test_valid_move(self):
        # Test case: Moving to a valid position
        print("Running test case: Moving to a valid position")
        self.assertTrue(self.knight.valid_move([2, 1]))

        # Test case: Moving to an invalid position
        print("Running test case: Moving to an invalid position")
        self.assertFalse(self.knight.valid_move([-1, 2]))

        # Test case: Moving to an invalid position
        print("Running test case: Moving to an invalid position")
        self.assertFalse(self.knight.valid_move([8, 8]))

    def test_move_to(self):
        # Test case: Moving to a valid position
        print("Running test case: Moving to a valid position")
        self.knight.move_to([2, 1])
        self.assertEqual(self.knight.start_pos, [2, 1])

        # Test case: Moving to an invalid position
        print("Running test case: Moving to an invalid position")
        self.assertRaisesRegex(ValueError, "Invalid move",
                               self.knight.move_to, [-1, 2])

        # Test case: Moving to an invalid position
        print("Running test case: Moving to an invalid position")
        self.assertRaisesRegex(ValueError, "Invalid move",
                               self.knight.move_to, [8, 8])


if __name__ == '__main__':
    unittest.main()
