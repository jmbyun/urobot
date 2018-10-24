from .position import Position
from .direction import Direction
from .piece import Piece

class Agent(Piece):
    def __init__(self, position=None, direction=None):
        super().__init__(position=position);
        self.direction = Direction('r') if direction is None else direction
        self.piece_type = 'agent'
        self.agent_type = 'marker'

    def to_dict(self): 
        return {
            **(super().to_dict()),
            'agent_type': self.agent_type,
            'direction': self.direction.to_char()
        }