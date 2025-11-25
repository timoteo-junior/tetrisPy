from colors import Colors
import pygame
from position import Position

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.columns_offset = 0
        self.rotation_state = 0
        self.color = Colors.get_cell_colors()

    def move(self, rows, columns):
        self.row_offset += rows
        self.columns_offset += columns

    def get_cells_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.columns_offset)
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        self.rotation_state -= 1    
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) - 1

    def draw(self, screen):
        tiles = self.get_cells_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size + 1, tile.row * self.cell_size + 1, 
            self.cell_size -1, self.cell_size -1)
            pygame.draw.rect(screen, self.color[self.id], tile_rect)