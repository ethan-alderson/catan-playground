from typing import List
from model.resource import Resource

class Player:
    
    def __init__(self, resources: List[Resource], vp: int):
        self.resources = resources
        vp = vp
        