import pygame
import random
import time

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
            cell = Cell(c, r, cell_size)
            cell.get_neighbors(row_count - 1, col_count - 1)
            row.append(cell)
        grid.append(row)
    return grid

def randomize_life():
    for r in range(row_count):
        for c in range(col_count):
            cell = grid[r][c]
            if random.random() >= 0.5:
                cell.is_alive = True

def update_grid_state():
    for cell in cells_to_track:
        if isinstance(cell, tuple):
            r, c = cell
            grid[r][c].update_state()

def calculate_next_generation():
    for cell in cells_to_track:
        if isinstance(cell, tuple):
            r, c = cell
            grid[r][c].count_live_neighbors(grid)
    update_grid_state()


cell_size = 5
row_count = window_height // cell_size
col_count = window_width // cell_size

grid = initialize_grid()
randomize_life()

cells_to_track = set()
cells_to_track_previous = set()
for r in range(row_count):
    for c in range(col_count):
        grid[r][c].draw(screen)
        if grid[r][c].is_alive:
            cells_to_track_previous.add((r, c))
            cells_to_track_previous.update(set(grid[r][c].neighbors))

generation = 0
start_time = time.time_ns()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # screen.fill(Color.BLACK.value)

    for cell in cells_to_track_previous:
        if isinstance(cell, tuple):
            r, c = cell
            grid[r][c].draw(screen)
            if grid[r][c].is_alive:
               cells_to_track.add((r, c))
               cells_to_track.update(set(grid[r][c].neighbors))
               
    print(len(cells_to_track))
    clock.tick(fps)
    pygame.display.flip()

    generation += 1
    print(generation)
    if generation % 100 == 0:
        stop_time = time.time_ns()
        run_time = (stop_time - start_time) / 1000000000
        print(f"Took {run_time} seconds!")

        start_time = time.time_ns()
        # running = False

    calculate_next_generation()
    cells_to_track_previous = cells_to_track
    cells_to_track = set()


pygame.quit()