from typing import List, Set, Optional
from model.resource import Resource

class Player:
    
    def __init__(self, resources: List[Resource], vp: int, owned_vertices: Optional[Set[int]] = None):
        self.resources = resources
        self.vp = vp
        self.owned_vertices = owned_vertices or []

    def snapshot(self) -> dict:
        return {
            "resources": [resource.name for resource in self.resources],
            "vp": self.vp,
            "owned_vertices": self.owned_vertices,
        }
        