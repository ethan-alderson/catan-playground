from typing import List
from enum import Enum

class Vertex:
    
    # vertex has optional owner player, 
    
    
    def __init__(self, vertex_id, type: VertexType, adjacent_tiles: List[]):
        self.id = vertex_id
        self.adjacent_tiles: List[int] = []
        
        # 
        self.owner = None
    

class VertexType(Enum):
    EMPTY = 0
    SETTLEMENT = 1
    CITY = 2