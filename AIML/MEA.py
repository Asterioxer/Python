# Grid dimensions (5x5)
GRID_SIZE = 5

# Initial Position of the robot
current_position = [0, 0]  # Robot starts at (0, 0)
goal_position = [4, 4]     # Goal is at (4, 4)

# Loop until the robot reaches the goal
while current_position != goal_position:
    # Print the current position and goal position
    print("Current Position:", current_position)
    print("Goal Position:", goal_position)
    
    # Calculate the difference in x and y coordinates
    x_diff = goal_position[0] - current_position[0]
    y_diff = goal_position[1] - current_position[1]
    
    # Choose action to minimize the most significant difference
    if abs(x_diff) > abs(y_diff):
        if x_diff > 0:
            current_position[0] += 1  # Move right
        elif x_diff < 0:
            current_position[0] -= 1  # Move left
    else:
        if y_diff > 0:
            current_position[1] += 1  # Move down
        elif y_diff < 0:
            current_position[1] -= 1  # Move up

    # Print the grid after each move
    grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    x, y = current_position
    grid[x][y] = 'R'
    
    for row in grid:
        print(" ".join(row))
    print("\n")
    
# Print final goal reached
print("Goal reached at:", current_position)
 