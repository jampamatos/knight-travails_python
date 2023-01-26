import subprocess
import sys

class Messages:
  @staticmethod
  def clear_screen():
    subprocess.run("clear")
  
  def welcome_msg():
    Messages.clear_screen()
    print('')
    print('                 WELCOME TO THE KNIGHT TRAVAILS PROJECT                 ')
    print('')
    print("The 'Knight Travalis Project' is based on the fact that a knight in")
    print("chess can move to any square on the standard 8x8 chess board from any")
    print("other square on the board, given enough turns.")
    print('')
    print("Its basic move is two steps forward and one step to the side.")
    print("It can face any direction.")
    print('')
    print("The game will uses a shortest path algorithm to determine the")
    print("minimum number of moves the knight must make to reach the end")
    print("position from the start position.")
    print('')
    print("It's a fun and interactive way to visualize the unique")
    print("movement of the knight piece in chess and the many")
    print("possible paths it can take to reach a specific square on the board.")
    print('')
    print('')
  
  def quit_game():
    Messages.clear_screen()
    print("Thank you for playing!")
    print("Made by Jampa Matos")
    sys.exit()