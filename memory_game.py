"""
Memory Matching Game
CMPS-1100 Foundations of Programming Project
Sophia Israel

This is the starter file for my Memory Matching Game project.
Core features implemented:
- Generates a shuffled 4x4 board
- Cards start hidden
- Player selects multiple cards each turn
- Matching system for 2 or 4 cards
- Attempt counter
- Cards reveal before match check
- Matched cards stay visible
"""

import random

def create_board(match_size):
    values = []

    if match_size == 2:
        for i in range(1, 9):
            values.extend([i, i])

    elif match_size == 4:
        for i in range(1, 5):
            values.extend([i, i, i, i])

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


def all_matched(board):
    for row in board:
        for value, status in row:
            if status != "matched":
                return False
    return True


def get_valid_pick(board, selected_positions):
    while True:
        row_input = input("Row (0-3): ")
        if not row_input.isdigit():
            print("Invalid input. Try again.")
            continue
        r = int(row_input)

        col_input = input("Col (0-3): ")
        if not col_input.isdigit():
            print("Invalid input. Try again.")
            continue
        c = int(col_input)

        if not (0 <= r <= 3 and 0 <= c <= 3):
            print("Invalid input. Try again.")
            continue

        if (r, c) in selected_positions:
            print("You already picked that card this turn. Try again.")
            continue

        value, status = board[r][c]
        if status == "matched":
            print("That card is already matched. Try again.")
            continue

        return r, c


def main():
    print("Memory Matching Game")
    print("CMPS-1100 Foundations of Programming")
    print("Starter scaffold loaded successfully.")

    while True:
        match_input = input("How many cards to match? (2 or 4): ")
        if match_input.isdigit():
            match_size = int(match_input)
            if match_size in [2, 4]:
                break
        print("Invalid choice. Please enter 2 or 4.")

    board = create_board(match_size)
    display_board(board)

    guesses = 0

    while True:
        selected_positions = []

        for i in range(match_size):
            print(f"\nPick card {i + 1}:")
            r, c = get_valid_pick(board, selected_positions)
            selected_positions.append((r, c))

            value, _ = board[r][c]
            board[r][c] = (value, "revealed")
            display_board(board)

        guesses += 1
        print("\nAttempt #", guesses)

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

        display_board(board)

        if all_matched(board):
            print("\nCongratulations! You found all matches!")
            print("Total attempts:", guesses)
            break


if __name__ == "__main__":
    main()