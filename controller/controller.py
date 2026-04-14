import random

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
        self.player_action(player)

        # 4. Advance turn
        self.state.advance_turn()
        
    def roll_dice(self):
        return random.randint(1, 6) + random.randint(1, 6)
    
    
    def distribute_resources(self, roll):
        """
        TODO: connect to Board + intersections later
        """
        pass


    def player_action(self, player):
        """
        TODO: bot logic will plug in here
        """
        pass