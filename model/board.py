from typing import List

from model.tile import Tile
from model.vertex import Vertex
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
        
            
        self.vertices = [
        # Top point of each row-0 hex
        Vertex(0,  [0]),
        Vertex(1,  [1]),
        Vertex(2,  [2]),

        # Upper-left shoulders of row-0 hexes
        Vertex(3,  [0]),
        Vertex(4,  [0, 1]),
        Vertex(5,  [1, 2]),
        Vertex(6,  [2]),

        # Between row-0 and row-1
        Vertex(7,  [0, 3]),
        Vertex(8,  [0, 1, 4]),
        Vertex(9,  [1, 2, 5]),
        Vertex(10, [2, 6]),

        # Upper-left shoulders of row-1 hexes
        Vertex(11, [3]),
        Vertex(12, [0, 3, 4]),
        Vertex(13, [1, 4, 5]),
        Vertex(14, [2, 5, 6]),
        Vertex(15, [6]),

        # Between row-1 and row-2
        Vertex(16, [3, 7]),
        Vertex(17, [3, 4, 8]),
        Vertex(18, [4, 5, 9]),
        Vertex(19, [5, 6, 10]),
        Vertex(20, [6, 11]),

        # Upper-left shoulders of row-2 hexes
        Vertex(21, [7]),
        Vertex(22, [3, 7, 8]),
        Vertex(23, [4, 8, 9]),
        Vertex(24, [5, 9, 10]),
        Vertex(25, [6, 10, 11]),
        Vertex(26, [11]),

        # Between row-2 and row-3
        Vertex(27, [7]),
        Vertex(28, [7, 8, 12]),
        Vertex(29, [8, 9, 13]),
        Vertex(30, [9, 10, 14]),
        Vertex(31, [10, 11, 15]),
        Vertex(32, [11]),

        # Upper-left shoulders of row-3 hexes
        Vertex(33, [7, 12]),
        Vertex(34, [8, 12, 13]),
        Vertex(35, [9, 13, 14]),
        Vertex(36, [10, 14, 15]),
        Vertex(37, [11, 15]),

        # Between row-3 and row-4
        Vertex(38, [12]),
        Vertex(39, [12, 13, 16]),
        Vertex(40, [13, 14, 17]),
        Vertex(41, [14, 15, 18]),
        Vertex(42, [15]),

        # Upper-left shoulders of row-4 hexes
        Vertex(43, [12, 16]),
        Vertex(44, [13, 16, 17]),
        Vertex(45, [14, 17, 18]),
        Vertex(46, [15, 18]),

        # Lower sides of row-4 hexes
        Vertex(47, [16]),
        Vertex(48, [16, 17]),
        Vertex(49, [17, 18]),
        Vertex(50, [18]),

        # Bottom points of row-4 hexes
        Vertex(51, [16]),
        Vertex(52, [17]),
        Vertex(53, [18]),
        ]
        
        self.vertex_neighbors = {
            0:  [3, 4],
            1:  [4, 5],
            2:  [5, 6],
            3:  [0, 7],
            4:  [0, 1, 8],
            5:  [1, 2, 9],
            6:  [2, 10],
            7:  [3, 11, 12],
            8:  [4, 12, 13],
            9:  [5, 13, 14],
            10: [6, 14, 15],
            11: [7, 16],
            12: [7, 8, 17],
            13: [8, 9, 18],
            14: [9, 10, 19],
            15: [10, 20],
            16: [11, 21, 22],
            17: [12, 22, 23],
            18: [13, 23, 24],
            19: [14, 24, 25],
            20: [15, 25, 26],
            21: [16, 27],
            22: [16, 17, 28],
            23: [17, 18, 29],
            24: [18, 19, 30],
            25: [19, 20, 31],
            26: [20, 32],
            27: [21, 33],
            28: [22, 23, 34],
            29: [23, 24, 35],
            30: [24, 25, 36],
            31: [25, 26, 37],
            32: [26, 37],
            33: [27, 28, 38],
            34: [28, 29, 39],
            35: [29, 30, 40],
            36: [30, 31, 41],
            37: [31, 32, 42],
            38: [33, 43],
            39: [34, 35, 44],
            40: [35, 36, 45],
            41: [36, 37, 46],
            42: [37, 46],
            43: [38, 39, 47],
            44: [39, 40, 48],
            45: [40, 41, 49],
            46: [41, 42, 50],
            47: [43, 51],
            48: [44, 45, 52],
            49: [45, 46, 53],
            50: [46, 53],
            51: [47, 48, 52],
            52: [48, 49, 51],
            53: [49, 50, 52],
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