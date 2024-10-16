import random

board = []

for space in range(0,5):
    board.append(["."] * 5)

def print_board(board):
    for space in board:
        print(" ".join(space))
    

    
def generate_guess():
    return random.randint(0, 5), random.randint(0, 5)

def guess_location():   
    user_column_guess = int(input("Enter a Column Number: "))
    user_row_guess = int(input("Enter a Row Number: "))
    return user_column_guess,user_column_guess

def validate_location_guess(user_guess, computer_location):
    if user_guess == computer_location:
        print("Battleship has been sunk, Congratulations!")
        print_board(board) 
    else:
        print("No hit! Better luck next time.")
        board[user_guess[0]][user_guess[1]] = "X"
        print_board(board)
        
def main():
    computer_location = generate_guess()
    print_board(board)
    
    user_guess = guess_location()
    validate_location_guess(user_guess, computer_location)
     
if __name__ == "__main__":     
    main()