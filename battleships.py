# Imported the random library to help in creating a randon integer for computer
import random

# Encapsulated the game into a class for easier user functionality
class Battleships:
    # Generates board, places ships on the board, and provides the amount of guesses
    def __init__(self):
        self.user_board = [["."] * 5 for _ in range(5)]
        self.computer_board = [["."] * 5 for _ in range(5)]
        self.user_ships = self.place_ships()
        self.computer_ships = self.place_ships()
        self.max_attempts = 5
        self.attempts = 0
        
    # Displays welcome message with instructions on how to play
    def welcome(self):
        print("Hello and welcome to my Battleships game!")
        print("You will have 5 ships across a 5X5 board.")
        print("You will have 5 guesses to guess the locations of the ships!")
        print("Ready.. set.. GO!")
        print(" ")

    # Displays the board to the terminal
    def print_board(self, board):
        for row in board:
            print(" ".join(row))

    # Places the ships on the board and generates the computers location
    def place_ships(self):
        ships = set()
        while len(ships) < 5:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
            ships.add((row, col))
        return ships

    # Urges the user to type their guesses for the ships to the board
    def guess_entry(self):
        while True:
            try:
                # Asks the user to guess the row they believe the ship is on
                user_row_guess = int(input("Enter a Row Number: "))
                
                # Asks the user to guess the row they believe the ship is on
                user_column_guess = int(input("Enter a Column Number: "))
                
                # If invalid output is placed on the board the user will be directed to use the correct integers
                if 0 <= user_row_guess <= 4 and 0 <= user_column_guess <= 4:
                    return user_row_guess, user_column_guess
                else:
                    print("Please enter numbers between 0 and 4.")
            except ValueError:
                print("Invalid input. Please enter integers only.")

    # Validated the users output
    def validate_user_location_guess(self, user_row_guess, user_column_guess):
        if self.computer_board[user_row_guess][user_column_guess] in ["X", "/"]:
            
            # If the location has already been guessed the user will have another chance to guess
            print("You've already guessed that location! Try again.")
            return False

        # When the users guess is correct they'll receive a message advising of this
        if (user_row_guess, user_column_guess) in self.computer_ships:
            print("Battleship has been sunk, Congratulations!")
            self.computer_board[user_row_guess][user_column_guess] = "/"
            self.computer_ships.remove((user_row_guess, user_column_guess))  # Remove the sunk ship
            self.print_board(self.computer_board)
            return True
        
        # When the users guess is incorrect they'll receive a message advising of this
        else:
            print("No hit! Better luck next time.")
            self.computer_board[user_row_guess][user_column_guess] = "X"
            self.print_board(self.computer_board)
            return False
    
    # Computer guesses location of ships on the users board
    def computer_guess(self):
        # Computer guesses the coordiates of the users ships
        row, col = random.randint(0, 4), random.randint(0, 4)
        while self.user_board[row][col] in ["x", "/"]:
            row, col = random.randint(0, 4), random.randint(0, 4)
        
        # If a ship is hit a message will display to the terminal
        if (row, col) in self.user_ships:
            print("Computer hit your ship!")
            self.user_board[row][col] = "/"
            self.user_ships.remove((row, col))
            
        # If the computer misses a message will display to the terminal
        else:
            print("Computer didn't hit one of your ships!")
            self.user_board[row][col] = "X"

    def play_game(self):
        self.welcome()
        
        # Allows the user to guess as long as the number of attempts is below the max amount
        while self.attempts < self.max_attempts and self.user_ships and self.computer_ships:
            user_row_guess, user_column_guess = self.guess_entry()
            self.validate_user_location_guess(user_row_guess, user_column_guess)
            self.attempts += 1
                
            # If all ships are sunk
            if not self.computer_ships:  
                print("You got them all, you won!")
                return
            
            # The computer takes their turn
            self.computer_guess()
        
            # Game over alert for if the user has lost
            if not self.user_ships:
                print("All of your ships have been sunk, Game Over!")
                return
    
        print("GAME OVER!")
        print("User Board:")
        self.print_board(self.user_board)
        print("Computers board:")
        self.print_board(self.computer_board)

        
# Calls the functions in the main function
def main():
    game = Battleships()
    game.play_game()

if __name__ == "__main__":
    main()
