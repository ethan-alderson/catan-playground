from dataclasses import dataclass
from typing import Optional, Tuple, Callable, TYPE_CHECKING

from enum import Enum

if TYPE_CHECKING:
    from model.gamestate import GameState
    from model.player import Player

class ActionType(Enum):
    BUILD_SETTLEMENT = "build_settlement"
    BUILD_ROAD = "build_road"
    PASS = "pass"

@dataclass
class Action:
    type: ActionType
    
    # placement
    vertex: Optional[int] = None
    edge: Optional[Tuple[int, int]] = None  # (v1, v2)


# Action Handlers - extensible handler registry
def _apply_build_settlement(game_state: "GameState", action: "Action", player: "Player"):
    """Handle building a settlement."""
    if action.vertex is None:
        raise ValueError("Settlement build requires vertex")
    
    vertex = game_state.board.vertices[action.vertex]
    if vertex.owner is not None:
        raise ValueError(f"Vertex {action.vertex} is already owned")
    
    # TODO: Check resources, adjacency rules, etc.
    vertex.owner = player
    vertex.value = 1  # settlement
    player.owned_vertices.append(action.vertex)
    player.vp += 1
    print(f"Player built settlement at vertex {action.vertex}")


def _apply_build_road(game_state: "GameState", action: "Action", player: "Player"):
    """Handle building a road."""
    # TODO: Implement road building logic
    print(f"Player built road (not implemented yet)")


def _apply_pass(game_state: "GameState", action: "Action", player: "Player"):
    """Handle pass action."""
    print(f"Player passed")


# Handler registry - map action types to their handler functions
ACTION_HANDLERS: dict[ActionType, Callable] = {
    ActionType.BUILD_SETTLEMENT: _apply_build_settlement,
    ActionType.BUILD_ROAD: _apply_build_road,
    ActionType.PASS: _apply_pass,
}