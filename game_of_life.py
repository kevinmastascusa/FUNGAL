import pygame
from numpy import random, sum, copy

# Set up the dimensions of the grid
grid_width = 800
grid_height = 600
cell_size = 10
num_cols = grid_width // cell_size
num_rows = grid_height // cell_size

# Set up Pygame display
pygame.init()
window = pygame.display.set_mode((grid_width, grid_height))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()

# Initialize the grid with random cell states
grid = random.choice([0, 1], (num_rows, num_cols), p=[0.8, 0.2])

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255))

    # Create a copy of the grid to update in each iteration
    next_grid = copy(grid)

    # Iterate over each cell in the grid
    for row in range(num_rows):
        for col in range(num_cols):
            cell_state = grid[row, col]
            num_neighbors = sum(grid[max(0, row - 1):min(row + 2, num_rows), max(0, col - 1):min(col + 2, num_cols)]) - cell_state

            # Apply the rules of the Game of Life
            if cell_state == 0 and num_neighbors == 3:
                next_grid[row, col] = 1
            elif cell_state == 1 and (num_neighbors < 2 or num_neighbors > 3):
                next_grid[row, col] = 0

            # Draw the cell on the Pygame display
            cell_color = (0, 0, 0) if cell_state == 1 else (255, 255, 255)
            pygame.draw.rect(window, cell_color, (col * cell_size, row * cell_size, cell_size, cell_size))

    # Update the grid for the next iteration
    grid = copy(next_grid)

    pygame.display.flip()
    clock.tick(10)  # Adjust the speed of the game (number of generations per second)

pygame.quit()
