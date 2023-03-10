class ChessBoard:
    size = None

    def __init__(self, size=8):
        self.set_size(size)
        self.board = [[{'x': x, 'y': y, 'steps': 0}
                       for x in range(self.size)] for y in range(self.size)]
        self.knight = None

    def is_valid(self, x, y):
        return (0 <= x < self.size) and (0 <= y < self.size)

    def show_board(self, knight):
        print("   A  B  C  D  E  F  G  H")
        for i in range(self.size):
            row = f"{i+1} "
            for j in range(self.size):
                if (i+j) % 2 == 0:
                    if i == knight.start_pos[0] and j == knight.start_pos[1]:
                        row += "♞ "
                    else:
                        row += "## "
                else:
                    if i == knight.start_pos[0] and j == knight.start_pos[1]:
                        row += "♞ "
                    else:
                        row += "   "
            print(row + f" {i+1}")
        print("   A  B  C  D  E  F  G  H")

    def set_knight(self, knight):
        self.knight = knight

    @classmethod
    def set_size(cls, size):
        cls.size = size
