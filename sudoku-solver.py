"""Sudoku Solver

A program to solve for the popular puzzle game, Sudoku"""

import time
import sys


def solve(board):
    """Solves the Sudoku puzzle"""

    # Check if there is still an empty space
    if not empty_space(board):
        return True
    else:
        row, col = empty_space(board)  # Assign the empty location

    # Assign a number to the empty space
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num

            if solve(board):
                return True

            # Reset the number if it failed
            board[row][col] = 0

    return False


def make_board():
    """Opens the the file and makes the board"""

    # Also checks if the user gave a file
    try:
        with open(sys.argv[1], "r") as input_file:
            board = []
            for x in range(9):
                row = []
                for num in input_file.readline():
                    if num != "\n":
                        row.append(int(num))
                board.append(row)
        return board
    except IOError:
        print sys.argv[1] + " is not a file"
        sys.exit(2)


def print_board(board):
    """Prints the board"""
    for row in board:
        print " ".join(str(num) for num in row)


def used_in_row(board, row, num):
    """Checks if num is present in the current row"""
    for col in range(9):
        if board[row][col] == num:
            return True
    return False


def used_in_col(board, col, num):
    """Checks if num is present in the current col"""
    for row in range(9):
        if board[row][col] == num:
            return True
    return False


def used_in_box(board, start_box_row, start_box_col, num):
    """Checks if num is present in the current 3x3 box"""
    for row in range(3):
        for col in range(3):
            if board[row + start_box_row][col + start_box_col] == num:
                return True
    return False


def is_safe(board, row, col, num):
    """Checks if the num is present in the current row, col and 3x3 box"""
    if (not used_in_row(board, row, num) and
            not used_in_col(board, col, num) and
            not used_in_box(board, row - row % 3, col - col % 3, num)):
        return True
    return False


def empty_space(board):
    """Finds the empty space in the board starting from the top left corner
    going right"""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return False


def main():

    # Check if the user given a Sudoku file
    if len(sys.argv) != 2:
        print "usage: sudoku-solver.py [Sudoku File]"
        sys.exit(1)

    board = make_board()  # Make the board

    print "Input:"
    print_board(board)
    print "------------------"

    start = time.time()

    # Print the solution (if available) and the time it took to solve it
    if solve(board):
        end = time.time()
        print "Solution (" + str(round(end - start, 4)) + " seconds):"
        print_board(board)
    else:
        print "No solution exist"

main()
