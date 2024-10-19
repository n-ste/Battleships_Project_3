# Imported the random library to help in creating a random integer for computer
import random


# Encapsulated the game into a class for easier user functionality
class Battleships:
    # Generates board
    # Places ships on the board
    # Provides the amount of guesses
    def __init__(self):
        self.usr_board = [["."] * 5 for _ in range(5)]
        self.cmptr_board = [["."] * 5 for _ in range(5)]
        self.usr_ships = self.place_ships()
        self.cmptr_ships = self.place_ships()
        self.max_att = 5
        self.att = 0

    # Displays welcome message
    # Provides instructions on how to play
    def welcome(self):
        print("Hello and welcome to my Battleships game!")
        print("You will have 5 ships across a 5X5 board.")
        print("You will have 5 guesses to guess the locations of the ships!")
        print("Ready.. set.. GO!\n")

    # Displays the board to the terminal
    def print_board(self, board):
        for row in board:
            print(" ".join(row))

    # Places the ships on the board
    # Generates the computer's location
    def place_ships(self):
        ships = set()
        while len(ships) < 5:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
            ships.add((row, col))
        return ships

    # Urges the user to type their guesses for ships
    def guess_entry(self):
        while True:
            try:
                # Asks the user to guess the row they believe the ship is on
                usr_row_guess = int(input("Enter a Row Number:/n"))
                # Asks the user to guess the column they believe the ship is on
                usr_col_guess = int(input("Enter a Column Number:\n"))

                # If invalid output is placed on the board
                # User will be directed to use the correct integers
                if 0 <= usr_row_guess <= 4 and 0 <= usr_col_guess <= 4:
                    return usr_row_guess, usr_col_guess
                else:
                    print("Please enter numbers between 0 and 4.")
            except ValueError:
                print("Invalid input. Please enter integers only.")

    # Validates the user's output
    def validate_usr_location_guess(self, usr_row_guess, usr_col_guess):
        if self.cmptr_board[usr_row_guess][usr_col_guess] in ["X", "/"]:
            # If the location has already been guessed
            # User will have another chance to guess
            print("You've already guessed that location! Try again.")
            return False

        # When the user will receive message advising of this
        if (usr_row_guess, usr_col_guess) in self.cmptr_ships:
            print("Battleship has been sunk! Congratulations!")
            self.cmptr_board[usr_row_guess][usr_col_guess] = "/"

            # Removes the sunk ship
            self.cmptr_ships.remove((usr_row_guess, usr_col_guess))
            self.print_board(self.cmptr_board)
            return True

        # When the user's guess is incorrect, they'll receive a message
        else:
            print("No hit! Better luck next time.")
            self.cmptr_board[usr_row_guess][usr_col_guess] = "X"
            self.print_board(self.cmptr_board)
            return False

    # Computer guesses location of ships on the user's board
    def cmptr_guess(self):
        # Computer guesses the coordinates of the user's ships
        row, col = random.randint(0, 4), random.randint(0, 4)
        while self.usr_board[row][col] in ["x", "/"]:
            row, col = random.randint(0, 4), random.randint(0, 4)

        # If a ship is hit, a message will display to the terminal
        if (row, col) in self.usr_ships:
            print("Computer hit your ship!")
            self.usr_board[row][col] = "/"
            self.usr_ships.remove((row, col))
        # If the computer misses, a message will display to the terminal
        else:
            print("Computer didn't hit one of your ships!")
            self.usr_board[row][col] = "X"

    def play_game(self):
        self.welcome()

        # Allows the user to guess
        # As long as the number of attempts is below the max amount
        while self.att < self.max_att and self.usr_ships and self.cmptr_ships:
            usr_row_guess, usr_col_guess = self.guess_entry()
            self.validate_usr_location_guess(usr_row_guess, usr_col_guess)
            self.att += 1

            # If all ships are sunk
            if not self.cmptr_ships:
                print("You got them all! You won!")
                return

            # The computer takes their turn
            self.cmptr_guess()

            # Game over alert for if the user has lost
            if not self.usr_ships:
                print("All of your ships have been sunk. Game Over!")
                return

        print("GAME OVER!")
        print("User Board:")
        self.print_board(self.usr_board)
        print("Computer's board:")
        self.print_board(self.cmptr_board)


# Calls the functions in the main function
def main():
    game = Battleships()
    game.play_game()


if __name__ == "__main__":
    main()
