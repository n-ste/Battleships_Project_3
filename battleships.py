import random

board = []

# Initialize the board
for space in range(0, 5):
    board.append(["."] * 5)

def print_board(board):
    for space in board:
        print(" ".join(space))
        
def generate_row_guess():
    return random.randint(0, 4)
    
def generate_column_guess():
    return random.randint(0, 4)
    
computer_row = generate_row_guess()
computer_column = generate_column_guess()

def guess_location():   
    print(f"Computer's guess location: {computer_row}, {computer_column}")

def guess_entry():
    while True:
        try:
            user_row_guess = int(input("Enter a Row Number: "))
            user_column_guess = int(input("Enter a Column Number: "))
            if 0 <= user_row_guess <= 4 and 0 <= user_column_guess <= 4:
                return user_row_guess, user_column_guess
            else:
                print("Please enter numbers between 0 and 4.")
        except ValueError:
            print("Invalid input. Please enter integers only.")

def validate_location_guess(user_row_guess, user_column_guess):
    if user_row_guess == computer_row and user_column_guess == computer_column:
        print("Battleship has been sunk, Congratulations!")
        board[user_row_guess][user_column_guess] = "/"
    else:
        print("No hit! Better luck next time.")
        board[user_row_guess][user_column_guess] = "X"
        
    print_board(board)

def main():
    guess_location()
    user_row_guess, user_column_guess = guess_entry()
    validate_location_guess(user_row_guess, user_column_guess)

if __name__ == "__main__":     
    main()