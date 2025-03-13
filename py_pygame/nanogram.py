import numpy as np
import random

def generate_nanogram():
    # Generate a 3x3 matrix with 0s and 1s as its elements
    grid = np.random.randint(2, size=(3, 3))

    # 3 across clues and 3 down clues
    across_clues = []
    down_clues = []

    # Step 1: For the across clues
    # Take the sum of each row in the matrix
    for i in range(3):
        across_clues.append(sum(grid[i]))

    # Step 2: For the down clues
    # Transpose the matrix and take the sum of each column in the transposed matrix
    column_sum = np.sum(grid, axis=0)
    for i in range(3):
        down_clues.append(column_sum[i])

    # Print the grid and the clues
    print("Grid:\n")
    print(grid)
    print("\nDown Clues:\n")
    print(down_clues)
    print("\nAcross Clues:\n")
    print(across_clues)

generate_nanogram()

