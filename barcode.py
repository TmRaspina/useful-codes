def check_square(square):
    """
    Check if a 3x3 square can be a valid corner square.
    """
    needed = [[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]]
    
    count = 1  # Start with one valid possibility
    for i in range(3):
        for j in range(3):
            if square[i][j] == 2:
                # If it's 2, it can be either 0 or 1
                count *= 2
            elif square[i][j] != needed[i][j]:
                # If it doesn't match and it's not 2, it's invalid
                return 0
    return count

def get_square(grid, top_left_x, top_left_y):
    """
    Get the 3x3 square from the grid starting at (top_left_x, top_left_y).
    """
    return [row[top_left_y:top_left_y+3] for row in grid[top_left_x:top_left_x+3]]

def count_valid_barcodes(grid):
    # Define the top left coordinates of the 4 corner 3x3 squares
    corners = [(0, 0), (0, 6), (6, 0), (6, 6)]
    
    total_count = 1
    for x, y in corners:
        square = get_square(grid, x, y)
        count = check_square(square)
        if count == 0:
            return 0
        total_count *= count
    
    return total_count

# Reading the input grid
grid = []
for _ in range(9):
    grid.append(list(map(int, input().strip())))

# Calculate the number of valid barcodes
result = count_valid_barcodes(grid)

# Print the result
print(result)
