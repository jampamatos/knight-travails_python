from square import Square

class ChessBoard:
    size = None

    def __init__(self):
        self.set_size(8)
        self.create_squares()

    def create_squares(self):
        self.board = [[Square(x, y) for x in range(self.size)] for y in range(self.size)]

    @classmethod
    def set_size(cls, size):
        cls.size = size
