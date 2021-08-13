from enum import Enum
import random

class TileState(Enum):
    EMPTY = 0
    NUMBER = 1
    BOMB = 2



class Coordinate:
    def __innit__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return self.x == other.x and self.y == other.y
        return False

class GameState:
    def __init__(self, grid, start):
        self.grid = grid
        self.row_count = len(self.grid)
        self.column_count = len(self.grid[0])
        self.start = start

    def get_tile(self, coord):
        return self.grid[coord.y][coord.x]

    def set_tile(self, coord, state):
        old_value = self.grid[coord.y][coord.x]
        self.grid[coord.y][coord.x] = state
        new_value = self.grid[coord.y][coord.x]
        return old_value, new_value

    def generate_bomb(self):
        while True:
            x = random.randint(0, self.width)
            y = random.randint(0, self.lenth - 1)
            if self.get_tile(Coordinate(x, y)) == TileState.EMPTY:
                self.set_tile(Coordinate(x, y), TileState.BOMB)
                return