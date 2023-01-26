from lib.chessboard import ChessBoard
from lib.knight import Knight
from lib.messages import Messages as messages

import time

# chessboard = ChessBoard()
# knight = Knight(chessboard)

# chessboard.show_board(knight)
# print(knight.find_valid_moves())
# knight.move_to((3,4))
# chessboard.show_board(knight)
# print(knight.find_valid_moves())
# print('Path is:')
# print(knight.find_shortest_path((6,6)))

def animate_path(path, steps, chessboard, knight):
    messages.clear_screen()
    print("Starting position")
    chessboard.show_board(knight)
    time.sleep(1)  # pause for 1 second
    for step in range(steps):
        messages.clear_screen()
        print(f"Move {step+1}")
        knight.move_to(path[step])
        chessboard.show_board(knight)
        time.sleep(1)


def start_game():
    chessboard = ChessBoard()
    knight = Knight(chessboard)
    messages.clear_screen()
    print('Starting the game...')
    print('')
    start_pos = (0,0)
    end_pos_co = (0,0)
    while True:
        start_pos = input("Please enter a starting position (e.g. A1, B5, C3) or 'Q' to quit: ").upper()
        if start_pos == "Q":
            messages.quit_game()
        elif start_pos in ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", 
                            "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", 
                            "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", 
                            "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", 
                            "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", 
                            "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", 
                            "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", 
                            "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8"]:
            knight.start_pos = (int(start_pos[1]) - 1, ord(start_pos[0]) - ord("A"))
        print('')
        chessboard.show_board(knight)
        print('')
        end_pos = input("Please enter a starting position (e.g. A1, B5, C3) or 'Q' to quit: ").upper()
        if end_pos == "Q":
            messages.quit_game()
        elif end_pos in ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", 
                           "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", 
                           "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", 
                           "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", 
                           "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", 
                           "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", 
                           "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", 
                           "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8"]:
            end_pos_co = (int(end_pos[1]) - 1, ord(end_pos[0]) - ord("A"))
            print ('')
            print('Calculating...')
            path, n = knight.find_shortest_path(end_pos_co)
            time.sleep(1)
            print(f"The Knight will arrive in {end_pos} in {n} moves.")
            animate_path(path, n, chessboard, knight)

messages.welcome_msg()
while True:
    user_input = input("Press 'P' to play or 'Q' to quit: ").upper()
    if user_input == 'P':
        start_game()
    elif user_input == 'Q':
        messages.quit_game()
        break
    else:
        print("Invalid input. Please enter 'P' to play or 'Q' to quit.")
