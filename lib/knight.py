class Knight:

    def __init__(self, chessboard, start_pos = [0,0]):
        self.chessboard = chessboard
        self.start_pos = start_pos
        self.visited = []

    def valid_move(self, pos):
        if pos[0] < 0 or pos[0] > 7 or pos[1] < 0 or pos[1] > 7:
            return False
        # check if the move was already made
        if pos in self.visited:
            return False
        return True

    def find_valid_moves(self, pos = None):
        if not pos:
            pos = self.start_pos
        valid_moves = []
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for move in moves:
            new_x = pos[0] + move[0]
            new_y = pos[1] + move[1]
            if self.valid_move([new_x, new_y]):
                valid_moves.append([new_y, new_x])
        return valid_moves

    def move_to(self, pos):
        if self.valid_move(pos):
            self.start_pos = pos
            self.visited.append(pos)
            return True
        else:
            return False

