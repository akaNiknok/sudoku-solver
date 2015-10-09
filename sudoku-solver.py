"""Sudoku Solver

A program to solve for the popular puzzle game, Sudoku"""

import random
import sys


def solve(board):

    if not empty_space(board):
        return True
    else:
        row, col = empty_space(board)

    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


def make_board():
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
    for row in board:
        print " ".join(str(num) for num in row)


def used_in_row(board, row, num):
    for col in range(9):
        if board[row][col] == num:
            return True
    return False


def used_in_col(board, col, num):
    for row in range(9):
        if board[row][col] == num:
            return True
    return False


def used_in_box(board, start_box_row, start_box_col, num):
    for row in range(3):
        for col in range(3):
            if board[row + start_box_row][col + start_box_col] == num:
                return True
    return False


def is_safe(board, row, col, num):
    if (not used_in_row(board, row, num) and
            not used_in_col(board, col, num) and
            not used_in_box(board, row - row % 3, col - col % 3, num)):
        return True
    return False


def empty_space(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return False


def main():
    if len(sys.argv) != 2:
        print "usage: sudoku-solver.py [Sudoku File]"
        sys.exit(1)

    board = make_board()

    print "Input:"
    print_board(board)
    print "------------------"

    if solve(board):
        print "Solution:"
        print_board(board)
    else:
        print "No solution exist"

main()
