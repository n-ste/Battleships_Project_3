
board = []

for i in range(0,10):
    board.append(["."] * 10)

def print_board(board):
    for i in board:
        print(" ".join(i))
    
def main():
    print_board(board)
    
main()