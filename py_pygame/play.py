import numpy as np
import random

def generate_nanogram(theme=None):
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

    # If a theme is specified:
    if theme is not None:
        # Convert the theme words to a list of lists, where each word is represented as a list of its letters
        theme_letters = [list(word) for word in theme]

        # Fill in the grid with the theme words by iterating through the grid and replacing 0s with the next letter from each word
        for i in range(3):
            for j in range(3):
                if grid[i, j] == 0:
                    # Replace the 0 with the next letter from the theme word
                    letter = theme_letters[i][j]
                    grid[i, j] = letter
        # Replace '0' with ' ' in the grid
        grid[grid == '0'] = ' '

    # Print the grid and the clues
    print("Grid:\n")
    print(grid)
    print("\nDown Clues:\n")
    print(down_clues)
    print("\nAcross Clues:\n")
    print(across_clues)

def solve_nanogram(grid, across_clues, down_clues):
    # Your code for solving the puzzle here.
    pass

# Use the functions like this:

# Generate a puzzle with a theme
generate_nanogram(theme=['cat', 'dog', 'bird', 'fish'])

# Solve the puzzle
solve_nanogram(grid, across_clues, down_clues)
