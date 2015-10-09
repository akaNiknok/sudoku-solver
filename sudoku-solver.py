"""Sudoku Solver

A program to solve for the popular puzzle game, Sudoku"""

import random
import sys

g_row = 0
g_col = 0


def make_board():
    try:
        with open(sys.argv[1], "r") as input_file:
            board = []
            for x in range(9):
                row = []
                for num in input_file.readline():
                    if num != "\n":
                        row.append(num)
                board.append(row)
        return board
    except IOError:
        print sys.argv[1] + " is not a file"
        sys.exit(2)


def print_board(board):
    for row in board:
        print " ".join(row)


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
    global g_row, g_col
    for g_row in range(9):
        for g_col in range(9):
            if board[g_row][g_col] == " ":
                return True
    return False


def main():
    if len(sys.argv) != 2:
        print "usage: sudoku-solver.py [Sudoku File]"
        sys.exit(1)

    board = make_board()

    print_board(board)

main()
