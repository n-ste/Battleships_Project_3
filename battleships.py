# Imported the random library to help in creating a randon integer for computer
import random

# Encapsulated the game into a class for easier user functionality
class Battleships:
    # Generates board, places ships on the board, and provides the amount of guesses
    def __init__(self):
        self.board = [["."] * 5 for _ in range(5)]
        self.ships = self.place_ships()
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
    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    # Places the ships on the board and generates the computers location
    def place_ships(self):
        ships = set()
        while len(ships) < 5:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
            ships.add((row, col))
        return ships

    # Prints location of the ships locations for so the assessor can check for validity
    def print_ship_locations(self):
        print("Current ship locations for validation:")
        for ship in self.ships:
            print(ship)
        print(" ")

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
    def validate_location_guess(self, user_row_guess, user_column_guess):
        if self.board[user_row_guess][user_column_guess] in ["X", "/"]:
            
            # If the location has already been guessed the user will have another chance to guess
            print("You've already guessed that location! Try again.")
            return False

        # When the users guess is correct they'll receive a message advising of this
        if (user_row_guess, user_column_guess) in self.ships:
            print("Battleship has been sunk, Congratulations!")
            self.board[user_row_guess][user_column_guess] = "/"
            self.ships.remove((user_row_guess, user_column_guess))  # Remove the sunk ship
            self.print_board()
            return True
        
        # When the users guess is incorrect they'll receive a message advising of this
        else:
            print("No hit! Better luck next time.")
            self.board[user_row_guess][user_column_guess] = "X"
            self.print_board()
            return False

    def play_game(self):
        self.welcome()
        
        # Print ship locations for the user
        self.print_ship_locations()
        
        # Allows the user to guess as long as the number of attempts is below the max amount
        while self.attempts < self.max_attempts and self.ships:
            user_row_guess, user_column_guess = self.guess_entry()
            if self.validate_location_guess(user_row_guess, user_column_guess):
                # If all ships are sunk
                if not self.ships:  
                    print("You got them all, you won!")
                    return
            self.attempts += 1
        # Lets the user know the game is over
        print("Game Over!")
        
# Calls the functions in the main function
def main():
    game = Battleships()
    game.play_game()

if __name__ == "__main__":
    main()
