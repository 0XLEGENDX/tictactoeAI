import random
import json


good = {}
bad = {}

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
        
def convert(row,col):
    
    if(row== 0 and col == 0):
        
        return 1
    elif(row== 0 and col == 1):
        
        return 2
    elif(row== 0 and col == 2):
        
        return 3
    elif(row== 1 and col == 0):
        
        return 4
    elif(row== 1 and col == 1):
        
        return 5
    elif(row== 1 and col == 2):
        
        return 6
    elif(row== 2 and col == 0):
        
        return 7
    elif(row== 2 and col == 1):
        
        return 8
    elif(row== 2 and col == 2):
        
        return 9

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, maximizing):
    if check_winner(board, "X"):
        return 1
    elif check_winner(board, "O"):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing:
        max_eval = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    eval = minimax(board, depth + 1, False)
                    board[row][col] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    eval = minimax(board, depth + 1, True)
                    board[row][col] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

def ai_move(board):
    best_move = None
    best_eval = float('-inf')
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "X"
                eval = minimax(board, 0, False)
                board[row][col] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)
    return best_move

def play_game():
    
    count = 10000
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Let's play Tic Tac Toe! You are 'O'.")
    print_board(board)

    while count:
        
        count-=1
        player_row, player_col = random.randint(0,2),random.randint(0,2)
        
        while(board[player_row][player_col] != " "):
            
            player_row, player_col = random.randint(0,2),random.randint(0,2)
        
        if board[player_row][player_col] == " ":
            board[player_row][player_col] = "O"
        else:
            print("Invalid move. Cell already taken.")
            continue

        if check_winner(board, "O"):
            print("Congratulations! You won!")
            break

        if is_board_full(board):
            print("It's a draw!")
            board = [[" " for _ in range(3)] for _ in range(3)]
            print("Let's play Tic Tac Toe! You are 'O'.")
        
        
        newboard = ""
        
        for j in board:
            
            newboard+= "".join(j)
        
        print(newboard)

        ai_row, ai_col = ai_move(board)
        board[ai_row][ai_col] = "X"
        
        good[newboard] = [convert(ai_row,ai_col)]
        
        f = open("train1","w")
        f.write(json.dumps(good))
        f.close()

        if check_winner(board, "X"):
            print("AI player wins!")
            board = [[" " for _ in range(3)] for _ in range(3)]
            print("Let's play Tic Tac Toe! You are 'O'.")
            
            
        print(count)
        
        
        
    
    
    


if __name__ == "__main__":
    play_game()
