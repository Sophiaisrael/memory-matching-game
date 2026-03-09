"""
Memory Matching Game
CMPS-1100 Foundations of Programming Project
Sophia Israel

This is the starter file for my Memory Matching Game project.
Core features implemented:
- Generates a shuffled 4x4 board
- Cards start hidden
- Player selects three cards each turn
- Triple matching system
- Attempt counter
- Cards reveal before match check
- Matched cards stay visible
"""





# TODO:
# Implement board setupcd ~
# Implement game loop
# Implement matching logic
# Implement reshuffle feature
# Implement scoring system

import random

def create_board():
    values = values = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6]
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
                print("*", end=" ")
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

def all_matched(board):
    for row in board:
        for value, status in row:
            if status != "matched":
                return False
    return True

def main():
    print("Memory Matching Game")
    print("CMPS-1100 Foundations of Programming")
    print("Starter scaffold loaded successfully.")
    board = create_board()
    display_board(board)



    guesses = 0

    while True:
        input_is_valid=False
        while not input_is_valid: 
            print("\nPick first card:")
            r1 = int(input("Row (0-3): "))
            c1 = int(input("Col (0-3): "))

            print("\nPick second card:")
            r2 = int(input("Row (0-3): "))
            c2 = int(input("Col (0-3): "))

            print("\nPick third card:")
            r3 = int(input("Row (0-3): "))
            c3 = int(input("Col (0-3): "))

            guesses += 1
            print("\nAttempt #", guesses)

            if guesses % 5 == 0:
                print("Reshuffling the board!")
                board = create_board()
                display_board(board)

            if r1==r2 and c1==c2:
                print("invalid input")
            else:
                input_is_valid=True


        board[r1][c1] = (board[r1][c1][0], "revealed")
        board[r2][c2] = (board[r2][c2][0], "revealed")
        board[r3][c3] = (board[r3][c3][0], "revealed")

        display_board(board)    
             
        val1, _ = board[r1][c1]
        val2, _ = board[r2][c2]
        val3, _ = board[r3][c3]

        if val1 == val2 == val3:
            print("Triple match found!")
            board[r1][c1] = (val1, "matched")
            board[r2][c2] = (val2, "matched")
            board[r3][c3] = (val3, "matched")
        else:
            print("Not a match.")
    
        board[r1][c1] = (val1, "hidden")
        board[r2][c2] = (val2, "hidden")
        board[r3][c3] = (val3, "hidden")    

        display_board(board)

        if all_matched(board):
            print("\nCongratulations! You found all matches!")
            print("Total attempts:", guesses)
            break
    


if __name__ == "__main__":
    main()
