board = ["1","2","3","4","5","6","7","8","9"]
def display_board (): 
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print() 

def make_move(player):
  while True:
    position = input(f"Player{player}, choose position 1-9:")
    if not position.isdigit():
      print("please enter a number between 1-9")
      continue 
    
    position = int(position)
    if position < 1 or position > 9: 
      print("please enter a number between 1-9")
      continue
    
    index = position - 1
    if board [index] == "X" or board [index] == "O":
      print("position occupied, try again")
      continue
    board [index] = player
    break
    

def check_winner():
    winning_combinations = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row

        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column

        [0, 4, 8],  # Diagonal
        [2, 4, 6]   # Diagonal
    ]
    for combination in winning_combinations:
      a = combination [0]
      b = combination [1]
      c = combination [2]
      if board [a] == board [b] == board [c] and board [a] in ["X" "O"]:
        return True

    return False

def check_draw ():
  for position in board:
    if position != "X" and position != "O":
      return False
    
  return True
    
    
print("Welcome To Tic Tac Toe")
print("Player X goes first")    
while True:
  display_board()
  make_move ("X")
  
  if check_winner():
    display_board()
    print("player X wins")
    break
    
  if check_draw():
    display_board()
    print("draw")
    break
  
  display_board()
  make_move ("O")

  if check_winner():
    display_board()
    print("player O wins")
    break
  
  if check_draw():
    display_board()
    print("draw")
    break
      



  