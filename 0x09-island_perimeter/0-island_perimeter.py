#!/usr/bin/python3
"""Solution to interview question"""


def island_perimeter(grid):
    """Calculates perimeter of an island
    Returns:
        int: Perimeter
    """
    grid_length = len(grid)
    len_count = 0
    prev_box = 0

    perimeter = 0

    for row in grid:
        for idx, col in enumerate(row):
            if col > prev_box:
                perimeter += 1
            if col < prev_box:
                perimeter += 1
            if len_count and idx < len(grid[len_count - 1]):
                if grid[len_count - 1][idx] < col:
                    perimeter += 1
            if len_count < grid_length - 1 and idx < len(grid[len_count + 1]):
                if grid[len_count + 1][idx] < col:
                    perimeter += 1
            prev_box = col
        len_count += 1
    return perimeter
