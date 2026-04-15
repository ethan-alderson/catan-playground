from typing import List
from enum import Enum

class Vertex:
    
    # vertex has optional owner player, 
    
    
    def __init__(self, vertex_id, adjacent_tiles: List[int]):
        self.id = vertex_id
        self.adjacent_tiles = adjacent_tiles
        self.owner = None
    

# class VertexType(Enum):
#     EMPTY = 0
#     SETTLEMENT = 1
#     CITY = 2