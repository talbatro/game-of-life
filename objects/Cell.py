import pygame
from utils.Color import Color

class Cell(object):

    def __init__(self, col, row, size, is_alive):
        self.col = col
        self.row = row
        self.size = size
        self.is_alive = is_alive
        self.neighbors = 0

        self.x = self.col * self.size
        self.y = self.row * self.size

    def draw(self, screen):
        if self.is_alive:
            pygame.draw.rect(screen, Color.WHITE.value, (self.x, self.y, self.size, self.size))
        else:
            pygame.draw.rect(screen, Color.BLACK.value, (self.x, self.y, self.size, self.size))
        # pygame.draw.rect(screen, Color.GRAY.value, (self.x, self.y, self.size, self.size), 1)

    def count_neighbors(self, grid, max_row, max_col):
        self.neighbors = 0
        if self.col != 0:
            start_col = -1
        else:
            start_col = 0
        
        if self.col != max_col:
            end_col = 1
        else:
            end_col = 0
       
        if self.row != 0:
            start_row = -1
        else:
            start_row = 0
        
        if self.row != max_row:
            end_row = 1
        else:
            end_row = 0

        for r in range(start_row, end_row + 1):
            for c in range(start_col, end_col + 1):
                if r == 0 and c == 0:
                    continue
                if grid[self.row + r][self.col + c].is_alive:
                    self.neighbors += 1
