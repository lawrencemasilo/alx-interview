#!/usr/bin/python3
"""
This stript solves the N queens problem.
"""


import sys


def is_safe(board, row, col, n):
    """
    determines whether it's safe for the queen to move

    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i in range(row + 1):
        if board[row - i][col - i] == 1:
            return False

    for k in range(n):
        i = row + k
        j = col - k
        if 0 <= i < n and 0 <= j < n and board[i][j] == 1:
            return False

    return True


def solve_nqueens2(board, col, n, result):
    """
    returns True if at least one solution is found, otherwise False.
    """
    if col == n:
        result.append(
                [[i, j] for i in range(n)
                    for j in range(n) if board[i][j] == 1]
                )
        return True

    util_result = False

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            util_result = solve_nqueens2(
                    board, col + 1, n, result
                    ) or util_result
            board[i][col] = 0

    return util_result


def solve_nqueens(n):
    """
    returns an array of solutions
    """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    result = []
    solve_nqueens2(board, 0, n, result)
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        solutions = solve_nqueens(n)
        """for solution in solutions:"""
        for i in range(len(solutions) - 1, -1, -1):
            print(solutions[i])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
