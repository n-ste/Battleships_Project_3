
board = []

for space in range(0,10):
    board.append(["."] * 10)

def print_board(board):
    for space in board:
        print(" ".join(space))
    

    
def guess_row(board):
    return 0, len(board) - 1

    guess_user_row = guess_row(board)

def guess_column(board):
    return 0, len(board[0]) - 1

    guess_user_column = guess_column(board)
    
def guess_location():   
    user_column_guess = input("Enter a Column Number: ")
    user_row_guess = input("Enter a Row Number: ")
    

    
def main():
    print_board(board)
    guess_location()
     
main()