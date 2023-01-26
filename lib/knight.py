class Knight:

    def __init__(self, chessboard, start_pos=[0, 0], steps=0):
        self.chessboard = chessboard
        self.start_pos = start_pos
        self.steps = steps

    def valid_move(self, move):
        x, y = move
        possible_moves = [[-1, -2], [-2, -1], [-2, 1],
                          [-1, 2], [1, -2], [2, -1], [2, 1], [1, 2]]
        for dx, dy in possible_moves:
            if self.chessboard.is_valid(x + dx, y + dy) and self.chessboard.is_valid(x, y):
                return True
        return False

    def move_to(self, target_pos):
        if self.valid_move(target_pos):
            self.start_pos = target_pos
        else:
            raise ValueError("Invalid move")
