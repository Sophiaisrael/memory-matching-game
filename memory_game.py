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

def create_board(match_size):
    values = []
    num_unique = 16 // match_size

    for i in range(1, num_unique + 1):
        values.extend([i] * match_size)

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
    match_size = int(input("How many cards to match? (2, 3, 4): "))
    board = create_board()
    display_board(board)



    guesses = 0

    while True:
        input_is_valid=False

        while not input_is_valid: 
            selected_positions = []

            for i in range(match_size):
                print(f"\nPick card {i+1}:")
                r = int(input("Row (0–3): "))
                c = int(input("Col (0–3): "))
                selected_positions.append((r, c))

            input_is_valid = True

        guesses += 1
        print("\nAttempt #", guesses)

        if guesses % 5 == 0:
            print("Reshuffling the board!")
            display_board(board)
            board = create_board(match_size)\
            
        for r, c in selected_positions:
            value, _ = board[r][c]
            board[r][c] = (value, "revealed")

        display_board(board)
        values = [board[r][c][0] for r, c in selected_positions]

        if all(v == values[0] for v in values):
            print("Match!")
            for r, c in selected_positions:
                value, _ = board[r][c]
                board[r][c] = (value, "matched")
        else:
            print("Not a match.")
            for r, c in selected_positions:
                value, _ = board[r][c]
                board[r][c] = (value, "hidden")

        if all_matched(board):
            print("\nCongratulations! You found all matches!")
            print("Total attempts:", guesses)
            break
    


if __name__ == "__main__":
    main()
