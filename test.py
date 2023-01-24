import unittest
from lib.square import Square

class TestSquare(unittest.TestCase):
  def test_is_valid(self):
    self.log('Running test_is_valid with x and y < size')
    s1 = Square(2,3,0)
    self.log('Running test_is_valid with x and y == size')
    s2 = Square(8,8,0)
    self.log('Running test_is_valid with negative numbers')
    s3 = Square(-1,-1,-1)
    self.log('Running test_is_valid with x and y == size - 1')
    s4 = Square(7, 7, 0)
    self.log('Running test_is_valid with x and y == 0')
    s5 = Square(0, 0, 0)
    self.log('Running test_is_valid with steps != 0')
    s6 = Square(2, 3, 1)
    self.assertTrue(s1.is_valid())
    self.assertFalse(s2.is_valid())
    self.assertFalse(s3.is_valid())
    self.assertTrue(s4.is_valid())
    self.assertTrue(s5.is_valid())
    self.assertTrue(s6.is_valid())
  
  def log(self, message):
    print(f'{message}')

if __name__ == '__main__':
  unittest.main()