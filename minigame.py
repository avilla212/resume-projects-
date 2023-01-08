import sys
import random 

# create our board for the game
board = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]

# make a move
def make_move(board, player):
    # show that its player 1's turn or player 2's turn
    print(f"Player {player}'s turn")
    # get the row and column from the user
    row = int(input("Enter the row: "))
    col = int(input("Enter the column: "))
    
    # check if the move is valid
    if board[row][col] == 0:
        board[row][col] = player
    else:
        print("Invalid move")
        make_move(board, player)
        
# check if the game is over
def check_win(board, player):
    # check if the player won by row
    for row in board:
        if all(cell == player for cell in row):
            return True
        
    # check if the player won by column
    for i in range(3):
        if all(board[row][i] == player for row in range(3)):
            return True
    
    # check if the player won by diagonal
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# check if the game is a draw
def check_draw(board):
    for row in board:
        for cell in row:
            if cell == 0:
                return False
    return True
def play_game(board):
    player = random.randint(1, 2)
    
    while True:
        for row in board:
            print(row)
        make_move(board,player)
        
        if check_win(board,player):
            print(f"Player {player} won!")
            break
        elif check_draw(board):
            print("Game is a draw")
            break 
        player = 1 if player == 2 else 2

play_game(board)

    
