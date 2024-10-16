import random

board = []

for space in range(0,10):
    board.append(["."] * 10)

def print_board(board):
    for space in board:
        print(" ".join(space))
    

    
def generate_guess():
    return random.randint(0, 9), random.randint(0, 9)

def guess_location():   
    user_guess = generate_guess()
    
    user_column_guess = int(input("Enter a Column Number: "))
    user_row_guess = int(input("Enter a Row Number: "))

def validate_location_guess(guess_location):
    if guess_location == generate_guess:
        print("Battleship has been sunk, Congratulations!") 
    else:
        print("No hit! Better luck next time.")
        
def main():
    print_board(board)
    guess_location()
    validate_location_guess(guess_location)
     
main()