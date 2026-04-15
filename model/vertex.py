from typing import List
from enum import Enum

class Vertex:    
    
    def __init__(self, vertex_id, adjacent_tiles: List[int]):
        self.id = vertex_id
        self.adjacent_tiles = adjacent_tiles
        self.owner = None
        self.value = 0