import random
import json

from model.action import Action, ActionType

class GameController:
    
    def __init__(self, game_state):
        self.state = game_state
        self.running = True
        
    def run(self, max_turns=50):
        """
        Main simulation loop.
        """
        while self.running and self.state.turn_number < max_turns:

            self.execute_turn()
            
        else:
            print(json.dumps(self.state.snapshot(), indent=4))
    
    
    def execute_turn(self):
        """
        Executes a single player's full turn.
        """

        player = self.state.get_current_player()

        # 1. Roll dice
        roll = self.roll_dice()
        self.state.set_last_roll(roll)

        print(f"[TURN {self.state.turn_number}] Player {self.state.curr_player_idx} rolled {roll}")

        # 2. Resource distribution (stub for now)
        self.distribute_resources(roll)

        # 3. Player action phase (stub bot)
        action = self.player_action(player)
        self.state.apply_action(action, player)

        # 4. Advance turn
        self.state.advance_turn()
        
    def roll_dice(self):
        return random.randint(1, 6) + random.randint(1, 6)
    
    
    def distribute_resources(self, roll):
        for i in range(0, 4):
            p = self.state.get_player(i)
            
            for v in p.owned_vertices:
                vertex = self.state.board.vertices[v]
                
                for tile_index in vertex.adjacent_tiles:
                    tile = self.state.board.tiles[tile_index]
                    
                    if tile.number == roll:
                        p.resources.append(tile.resource)
                        print(f'Distributed {tile.resource} to Player {i}')


    def player_action(self, player):
        print(f"Owned vertices: {player.owned_vertices}")
        
        # Currently we have random actions
        # Player 1 manual via print player 2-4 could make random for testing
    
        action_type = random.randint(0,2)
        print(f'action: {action_type}')
        if action_type == 0:
            v_idx = random.randint(0,53)
            return Action(type=ActionType.BUILD_SETTLEMENT, vertex=v_idx)
        else:
            return Action(type=ActionType.PASS)
            
            
        # action_type = input("Enter action (build/pass): ")
        
        # if action_type == "build":
        #     v_idx = int(input("Enter vertex index (0-53): "))
        #     return Action(type="build_settlement", vertex=v_idx)
        
        # return Action(type="pass")
    
    
        # if len(player.owned_vertices) < 1:
        #     v_idx = random.randint(0, 53)
        #     player.owned_vertices.append(v_idx)
        #     self.state.board.vertices[v_idx].owner = player
        #     self.state.board.vertices[v_idx].value = 1
            
