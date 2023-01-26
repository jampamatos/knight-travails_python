from collections import deque

class Knight:

    def __init__(self, chessboard, start_pos = (0,0)):
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
                valid_moves.append((new_y, new_x))
        return valid_moves

    def move_to(self, pos):
        if self.valid_move(pos):
            self.start_pos = pos
            self.visited.append(pos)
            return True
        else:
            return False
        
    def find_shortest_path(self, target_pos, start_pos = None):
        if not start_pos:
            start_pos = self.start_pos
        queue = deque([start_pos])
        visited = set()
        path_tracker = {start_pos: None}
        while queue:
            current_pos = queue.popleft()
            if current_pos == target_pos:
                break
            for next_pos in self.find_valid_moves(current_pos):
                if next_pos not in visited:
                    queue.append(next_pos)
                    visited.add(next_pos)
                    path_tracker[next_pos] = current_pos
        return self.reconstruct_path(path_tracker, start_pos, target_pos), len(self.reconstruct_path(path_tracker, start_pos, target_pos))

    def reconstruct_path(self, path_tracker, start_pos, target_pos):
        current_pos = target_pos
        path = []
        while current_pos != start_pos:
            path.append(current_pos)
            current_pos = path_tracker[current_pos]
        path.append(start_pos)
        return path[::-1]

