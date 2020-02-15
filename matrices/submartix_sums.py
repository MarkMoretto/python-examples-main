"""
Purpose: Run through a grid/matrix and sub each subgrid.
Date: 2020-02-15
Contributor: Mark Moretto

Example:

Matrix: 
  9  8  7
  6  5  4
  3  2  1
  
For subgrids of 2x2, we have the sum of values:
  9 8 6 5 = 28
  8 7 5 4 = 24
  6 5 3 2 = 16
  5 4 2 1 = 12
  Total --> 80
"""

def subgrid_sum(grid, n_rows=2, n_cols=2):
    """
    Sum the total of each sum of a subsection of a grid.
    parameters:
        n_rows (int): Number of rows to include
        n_cols (int): Number of columns to include
    """
    tot = 0
    subtot = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if i < n_rows:
                if j < n_cols:
                    subtot = 0
                    for r in range(n_rows):
                        for c in range(n_cols):
                            subtot += grid[r+i][c+j]
                    tot += subtot
    return tot
