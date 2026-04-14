from model.player import Player
from model.board import Board
from typing import List

class GameState:
    
    def __init__(self, board: Board, players: List[Player]):
        
        # core immutable world structure
        self.board = board
        
        # list of players and their hands
        self.players = players
        
        # tracking
        self.curr_player_idx = 0
        self.turn_number = 0
        self.last_roll = None

    # Define player access helpers        
    def get_current_player(self) -> Player:
        return self.players[self.curr_player_idx]


    def get_player(self, player_id: int) -> Player:
        return self.players[player_id]
    
    
    def advance_turn(self):
        self.curr_player_idx = (
            self.curr_player_idx + 1
        ) % len(self.players)

        self.turn_number += 1
        self.phase = "ROLL"
        self.last_roll = None
    
        
    def set_last_roll(self, roll: int):
        self.last_roll = roll


    # DEBUGGING INSPECTOR
    def snapshot(self) -> dict:
        """
        Useful later for logging, debugging, or ML encoding.
        Keep it simple for now.
        """
        return {
            "turn_number": self.turn_number,
            "current_player": self.curr_player_idx,
            "last_roll": self.last_roll,
            "phase": self.phase,
        }

    
    
