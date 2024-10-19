# Battleships

## How to Play

The rules of the game are quite simple. There will be a 5X5 board for the user and computer. Each board will have 5 ships on it, concealed to the user and computer.

The user and computer will have 5 attempts to guess the location of all 5 of their opponents ships.

If the user and computer guess the correct location of one of their opponents ships they'll receive a message on the terminal and their board will be updated to display this.

At the end of the 5 attempts, the user will be able to compare both boards to determine who won, along with a message advising the game is over.

## Design

In a traditional Battleships game the users would be playing on a 10X10 board, with some ships that span across different columns and rows. However, for simplicity I opted to make the board smaller at 5X5, with each ship only covering one row and column.

### Features

When the game starts the user will be given instructions on the game, these will advise:

* That there will be 5 ships spanned across a 5X5 board.

* The user will be advised they'll have 5 guesses to locate all of the ships on their opponents board.

* The user will then be met with an alert requesting they provide a number between 1 and 4 to choose the row.

* They'll then be advised to select a column number between 1 and 4.

* The user will then be given a message advising if they hit the computer ship or not, and also a message advising if the computer hit theirs. Their board will then be displayed on the terminal.

* This process will repeat 4 more times, at the end both boards will be displayed on the terminal allowing the user to see the overall score by assessing the boards and a "Game Over!" message will appear.

## Testing

### Validation

I tested the game in several ways:

* PEP8 Command Line
  * The issues that arose can be seen in the "Bugs" section below.

* CI Python Linter
  * For this, I followed the link and posted my Pthon code inside. When this came back I was given feedback advising that there were no errors with my code.
  * ![CI Python Linter](./assets/images/CI_linter.png)

* Playing the Game

#### Bugs

* PEP8 Command Line
  * To validate the Python code using the command line I first had to run "pip install pycodestyle" on the terminal.
  * I then had to run "pycodestyle run.py" to the terminal. 
  * This allowed me to see the errors that came with my code:
  * ![PEP8 Command Line Errors](./assets/images/PEP8_errors.png)

#### Solved

* PEP8 Command Line
  * The bug I had came from my lines of code exceeding the recommended amound of characters for Python code, this was mainly for comments.
  * I resolved this by separating my comments into sections and placeing them on the next row that followed.
  * Another issue was that my variable names contributed to the lenth of the lines of code. I resolved this by shortening these variable names.
  * Once amended, I ran "pycodestyle run.py" again and I was met with no feedback.
  * ![PEP8 Command Line Fix](./assets/images/PEP8_fix.png)

#### Remaining

* There were no bugs remaining.

## Deployment

## Credits

### Python

### Libraries

### Code Institute

### Youtube

