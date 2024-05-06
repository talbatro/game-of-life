import pygame
from utils.Color import Color

class Cell(object):

    ALIVE_LOOKUP = {
        0: False,
        1: False,
        2: True,
        3: True,
        4: False,
        5: False,
        6: False,
        7: False,
        8: False
    }

    DEAD_LOOKUP = {
        0: False,
        1: False,
        2: False,
        3: True,
        4: False,
        5: False,
        6: False,
        7: False,
        8: False
    }

    def __init__(self, col, row, size):
        self.col = col
        self.row = row
        self.size = size

        self.is_alive = False
        self.was_alive = False
        self.neighbors = []
        self.live_neighbors = 0

        self.x = self.col * self.size
        self.y = self.row * self.size

    def draw(self, screen):
        if self.was_alive != self.is_alive:
            if self.is_alive:
                pygame.draw.rect(screen, Color.WHITE.value, (self.x, self.y, self.size, self.size))
            else:
                pygame.draw.rect(screen, Color.BLACK.value, (self.x, self.y, self.size, self.size))
        pygame.draw.rect(screen, Color.GRAY.value, (self.x, self.y, self.size, self.size), 1)

    def update_state(self):
        self.was_alive = self.is_alive
        if self.is_alive:
            self.is_alive = self.ALIVE_LOOKUP.get(self.live_neighbors)
        else:
            self.is_alive = self.DEAD_LOOKUP.get(self.live_neighbors)
    
    def get_neighbors(self, max_row, max_col):
        self.neighbors = []

        start_col = -1 if self.col != 0 else 0
        end_col = 1 if self.col != max_col else 0
        start_row = -1 if self.row != 0 else 0
        end_row = 1 if self.row != max_row else 0

        for r in range(start_row, end_row + 1):
            for c in range(start_col, end_col + 1):
                if r == 0 and c == 0:
                    continue
                self.neighbors.append((self.row + r, self.col + c))

    def count_live_neighbors(self, grid):
        self.live_neighbors = 0
        for neighbor in self.neighbors:
            r, c = neighbor
            if grid[r][c].is_alive:
                self.live_neighbors += 1
