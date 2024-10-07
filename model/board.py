'''
Board class.

Board class is used to represent the board of the game.
It stores the tiles of the board along with their coordinates.
'''

from model.hextile import HexTile

class Board:
    def __init__(self, radius):
        self.radius = radius
        self.tiles = {}
        self._initialize_board()

    def _initialize_board(self):
        # Create tiles for each column
        for x in range(-self.radius + 1, self.radius):
            y_upper = (self.radius - 1) * 2 - abs(x)
            y_lower = -y_upper

            for y in range(y_lower, y_upper + 1, 2):
                self.tiles[(x, y)] = HexTile(x, y)


        # Set neighbors for each tile
        for (x, y), tile in self.tiles.items():
            neighbors = [
                ('north', (x, y + 2)),
                ('northeast', (x + 1, y + 1)),
                ('southeast', (x + 1, y - 1)),
                ('south', (x, y - 2)),
                ('southwest', (x - 1, y - 1)),
                ('northwest', (x - 1, y + 1))
            ]
            for direction, coords in neighbors:
                if coords in self.tiles:
                    tile.set_neighbor(direction, self.tiles[coords])

    def get_tile(self, x, y):
        return self.tiles.get((x, y))

    def __str__(self):
        output = f"Hexagonal board with radius {self.radius} and {len(self.tiles)} tiles.\n"
        for tile in self.tiles.values():
            output += f"{tile}"
        return output
    

