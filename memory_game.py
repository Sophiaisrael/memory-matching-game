"""
Memory Matching Game
CMPS-1100 Foundations of Programming Project
Sophia Israel

This is the starter file for my Memory Matching Game project.
Core features planned:
- Generate shuffled card pairs
- Display board to the user
- Allow card selection
- Match checking logic
- Reshuffle unmatched cards every 5 guesses
- Scoring system
- Optional hint feature
"""



# TODO:
# Implement board setup
# Implement game loop
# Implement matching logic
# Implement reshuffle feature
# Implement scoring system

import random

def create_board():
    values = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
    random.shuffle(values)

    board = []
    index = 0

    for r in range(4):
        row = []
        for c in range(4):
            row.append((values[index], "hidden"))
            index += 1
        board.append(row)

    return board

def display_board(board):
    print("\nCurrent Board:")
    for row in board:
        for card in row:
            value, status = card
            if status == "hidden":
                print(str(value)+"*", end=" ")
            else:
                print(value, end=" ")
        print()

def check_match(board, pos1, pos2):
            r1, c1 = pos1
            r2, c2 = pos2

            val1, _ = board[r1][c1]
            val2, _ = board[r2][c2]

            return val1 == val2

def mark_matched(board, pos1, pos2):
    r1, c1 = pos1
    r2, c2 = pos2

    val1, _ = board[r1][c1]
    val2, _ = board[r2][c2]

    board[r1][c1] = (val1, "matched")
    board[r2][c2] = (val2, "matched")
def main():
    print("Memory Matching Game")
    print("CMPS-1100 Foundations of Programming")
    print("Starter scaffold loaded successfully.")
    board = create_board()
    display_board(board)
    while True:
        input_is_valid=False
        while not input_is_valid: 
            print("\nPick first card:")
            r1 = int(input("Row (0-3): "))
            c1 = int(input("Col (0-3): "))

            print("\nPick second card:")
            r2 = int(input("Row (0-3): "))
            c2 = int(input("Col (0-3): "))

            if r1==r2 and c1==c2:
                print("invalid input")
            else:
                input_is_valid=True



             
        if check_match(board, (r1, c1), (r2, c2)):
            print("Match found!")
            mark_matched(board, (r1, c1), (r2, c2))
        else:
            print("Not a match.")
    

        display_board(board)

    


if __name__ == "__main__":
    main()
