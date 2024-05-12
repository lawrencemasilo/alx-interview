#!/usr/bin/python3
"""
An Island perimeter algorithm.
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid.
    """
    if grid and len(grid) < 101:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2
                else:
                    continue

        return perimeter
    return 0
