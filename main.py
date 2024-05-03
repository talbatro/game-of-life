import pygame
import random

from utils.Color import Color
from objects.Cell import Cell

pygame.init()

clock = pygame.time.Clock()
fps = 60

window_width = 1600
window_height = 1200
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Game of Life")

def initialize_grid():
    grid = []
    for r in range(row_count):
        row = []
        for c in range(col_count):
            row.append(Cell(c, r, cell_size, is_alive=True))
        grid.append(row)
    return grid

def randomize_life():
    for r in range(row_count):
        for c in range(col_count):
            cell = grid[r][c]
            if random.random() < 0.95:
               cell.is_alive = False
            else:
               cell.is_alive = True

def update_state():
    for r in range(row_count):
        for c in range(col_count):
            cell = grid[r][c]
            if cell.is_alive and (cell.neighbors == 2 or cell.neighbors == 3):
                cell.is_alive = True
            elif not cell.is_alive and cell.neighbors == 3:
                cell.is_alive = True
            else:
                cell.is_alive = False

def calculate_next_generation():
    for r in range(row_count):
        for c in range(col_count):
            grid[r][c].count_neighbors(grid, row_count - 1, col_count - 1)

    update_state()


cell_size = 10
row_count = window_height // cell_size
col_count = window_width // cell_size

grid = initialize_grid()
randomize_life()

generation = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill(Color.RED.value)

    for r in range(row_count):
        for c in range(col_count):
           grid[r][c].draw(screen)

    clock.tick(fps)
    pygame.display.flip()

    generation += 1
    calculate_next_generation()

pygame.quit()