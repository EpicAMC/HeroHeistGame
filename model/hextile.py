'''
HexTile class

HexTile class is used to represent a single tile on a hexagonal grid.
HexTile class stores the x and y coordinates of the tile, as well as the terrain type and occupant of the tile.
HexTile class also stores the neighbors of the tile, which are the tiles that are adjacent to it.
'''

class HexTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = {
            'north': None,
            'northeast': None,
            'southeast': None,
            'south': None,
            'southwest': None,
            'northwest': None
        }
        self.terrain = None
        self.occupant = None

    def set_neighbor(self, direction, tile):
        if direction in self.neighbors:
            self.neighbors[direction] = tile

    def get_neighbor(self, direction):
        return self.neighbors.get(direction)
    
    def __str__(self):
        output = f"HexTile({self.x}, {self.y})"
        output += "Adjacency list:\n"
        for direction, neighbor in self.neighbors.items():
            if neighbor:
                output += f"  {direction}: ({neighbor.x}, {neighbor.y})\n"
            else:
                output += f"  {direction}: None\n"
        output += "\n"
        return output


