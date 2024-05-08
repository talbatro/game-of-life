import random

from objects.Cell import Cell

class Grid(object):

    def __init__(self):
        self.cells = []
        self.cells_to_track = set()
        self.cells_to_track_previous = set()


    def initialize(self, cell_size, rows, cols):
        self.cell_size = cell_size
        self.rows = rows
        self.cols = cols

        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                cell = Cell(c, r, self.cell_size)
                cell.get_neighbors(self.rows - 1, self.cols - 1)
                row.append(cell)
            self.cells.append(row)

    def randomize_life(self, alpha):
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.cells[r][c]
                if random.random() >= alpha:
                    cell.is_alive = True
                    self.cells_to_track_previous.add((cell.row, cell.col))
                    self.cells_to_track_previous.update(set(cell.neighbors))

    def draw(self, screen):
        for cell_coord in self.cells_to_track_previous:
            if isinstance(cell_coord, tuple):
                r, c = cell_coord
                cell = self.cells[r][c]
                cell.draw(screen)
                if cell.is_alive:
                    self.cells_to_track.add((r, c))
                    self.cells_to_track.update(set(cell.neighbors))

    def calculate_next_generation(self):
        for cell_coord in self.cells_to_track:
            if isinstance(cell_coord, tuple):
                r, c = cell_coord
                self.cells[r][c].count_live_neighbors(self.cells)
        self.update_grid_state()
        self.cells_to_track_previous = self.cells_to_track
        self.cells_to_track = set()
        
        
    def update_grid_state(self):
        for cell_coord in self.cells_to_track:
            if isinstance(cell_coord, tuple):
                r, c = cell_coord
                self.cells[r][c].update_state()
    