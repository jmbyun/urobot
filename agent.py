from .position import Position
from .direction import Direction
from .piece import Piece

class Agent(Piece):
    def __init__(self, position=None, direction=None):
        super().__init__(position=position);
        self.direction = Direction('r') if direction is None else direction
        self.piece_type = 'agent'
        self.agent_type = 'marker'
        self.trace_color = None

    def set_trace(self, color='blue'):
        self.trace_color = color

    def to_dict(self): 
        return {
            **(super().to_dict()),
            'agent_type': self.agent_type,
            'trace_color': self.trace_color,
            'direction': self.direction.to_char()
        }