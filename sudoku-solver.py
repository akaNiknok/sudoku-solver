"""Sudoku Solver

A program to solve for the popular puzzle game, Sudoku"""

import random
import sys


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


def main():
    if len(sys.argv) != 2:
        print "usage: sudoku-solver.py [Sudoku File]"
        sys.exit(1)

    board = make_board()

main()
