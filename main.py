import pygame
import time

from utils.Color import Color
from objects.Grid import Grid
from objects.Cell import Cell

pygame.init()

clock = pygame.time.Clock()
fps = 60

window_width = 1600
window_height = 1200
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Game of Life")

cell_size = 5
rows = window_height // cell_size
cols = window_width // cell_size

grid = Grid()

grid.initialize(cell_size, rows, cols)
grid.randomize_life(0.5)

for r in range(rows):
    for c in range(cols):
        grid.cells[r][c].draw(screen)

generation = 0
start_time = time.time_ns()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # screen.fill(Color.BLACK.value)

    grid.draw(screen)
               
    print(len(grid.cells_to_track_previous))
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

    grid.calculate_next_generation()


pygame.quit()