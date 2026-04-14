from typing import List

from model.tile import Tile
from model.resource import Resource

class Board:
    
    def __init__(self, tiles: List[Tile]):
        self.tiles = tiles
        
        # maps tile index to neighbor indices
        self.tile_neighbors = {
        0:  [1, 3, 4],
        1:  [0, 2, 4, 5],
        2:  [1, 5, 6],

        3:  [0, 4, 7, 8],
        4:  [0, 1, 3, 5, 8, 9],
        5:  [1, 2, 4, 6, 9, 10],
        6:  [2, 5, 10, 11],

        7:  [3, 8, 12],
        8:  [3, 4, 7, 9, 12, 13],
        9:  [4, 5, 8, 10, 13, 14],
        10: [5, 6, 9, 11, 14, 15],
        11: [6, 10, 15],

        12: [7, 8, 13, 16],
        13: [8, 9, 12, 14, 16, 17],
        14: [9, 10, 13, 15, 17, 18],
        15: [10, 11, 14, 18],

        16: [12, 13, 17],
        17: [13, 14, 16, 18],
        18: [14, 15, 17],
    }
            
    #     0   1   2
    #   3   4   5   6
    # 7   8   9  10  11
    #   12  13  14  15
    #     16  17  18


        # key realization. Adjacency is hardcoded in terms of tile index. We can define tiles as a random list of length 19 but adjacency within the list is always the same with respect to the indices. 
        
# TEMPORARY FIXED BOARD FOR PROTOTYPING
class FixedBoardFactory:
    
    @staticmethod
    def create_tiles():

        return [
            Tile(Resource.WOOD, 8),
            Tile(Resource.BRICK, 5),
            Tile(Resource.SHEEP, 6),

            Tile(Resource.WHEAT, 9),
            Tile(Resource.ORE, 4),
            Tile(Resource.WOOD, 10),
            Tile(Resource.SHEEP, 3),

            Tile(Resource.BRICK, 8),
            Tile(Resource.WHEAT, 5),
            Tile(Resource.ORE, 9),
            Tile(Resource.WOOD, 4),

            Tile(Resource.SHEEP, 6),
            Tile(Resource.BRICK, 11),
            Tile(Resource.WHEAT, 3),
            Tile(Resource.ORE, 11),

            Tile(Resource.WOOD, 2),
            Tile(Resource.SHEEP, 12),
            Tile(Resource.WHEAT, 10),
            Tile(Resource.BRICK, 2),
        ]