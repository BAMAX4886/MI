import random

class Tile:
    def __init__(self, char=' '):
        self.char = char

class MapGenerator:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.tiles = [[Tile() for _ in range(width)] for _ in range(height)]
        self.generate_island()
        self.start_pos = (height // 2, width // 2)

    def generate_island(self):
        for y in range(self.height):
            for x in range(self.width):
                if random.random() < 0.8:
                    self.tiles[y][x].char = '.'
                else:
                    self.tiles[y][x].char = '~'

    def is_walkable(self, y, x):
        return self.tiles[y][x].char != '~'