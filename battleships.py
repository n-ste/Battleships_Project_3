# Imported the random library to help in creating a randon integer for computer
import random

# Introduction message
def welcome():
    print("Hello and welcome to my Battleships game!...")
    print(" ")
    print("Each player will have 5 ships across a 5X5 board.")
    print(" ")
    print("You will have 5 guesses to guess the location of the computer ships!")
    print(" ")
    print("Ready.. set.. GO!")
    print(" ")
# Empty array for the player board
board = []

# Initialize the board
for space in range(0, 5):
    board.append(["."] * 5)

# Prints the board and removes square brackets
def print_board(board):
    for space in board:
        print(" ".join(space))

# Computer generates a row value        
def generate_row_guess():
    return random.randint(0, 4)

# Computer generates a column value       
def generate_column_guess():
    return random.randint(0, 4)
    
computer_row = generate_row_guess()
computer_column = generate_column_guess()
    
# Displays the computers row and column values for validation purposes
def guess_location():   
    print(f"Computer's guess location: {computer_row}, {computer_column}")

# Instructs the user to input their guess for the location of the computers ships
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

# Provides validation for the users guess of the computers ships
def validate_location_guess(user_row_guess, user_column_guess):
    if board[user_row_guess][user_column_guess] in ["X", "/"]:
        print("You've already guessed that location! Try again.")
        
    if user_row_guess == computer_row and user_column_guess == computer_column:
        print("Battleship has been sunk, Congratulations!")
        board[user_row_guess][user_column_guess] = "/"
    else:
        print("No hit! Better luck next time.")
        board[user_row_guess][user_column_guess] = "X"
            
    print_board(board)
    
# Creates the loop so the player can play and updates the board after each play    
def game_over():
    game_over = False
    attempts = 0
    max_attempts = 4
    while not game_over and attempts < max_attempts:
        guess_location()
        user_row_guess, user_column_guess = guess_entry()
        game_over = validate_location_guess(user_row_guess, user_column_guess)
        attempts += 1  
        
# Functions added to main for easier log of called functions
def main():
    welcome()
    guess_location()
    user_row_guess, user_column_guess = guess_entry()
    validate_location_guess(user_row_guess, user_column_guess)
    game_over()

# Calls main function
if __name__ == "__main__":     
    main()