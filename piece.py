from .position import Position
from .direction import Direction

class Piece(object):
    def __init__(self, position=None):
        self.id = None
        self.world = None
        self.piece_type = 'piece'
        self.position = Position(0, 0) if position is None else position

    def to_dict(self): 
        return {
            'id': self.id,
            'piece_type': self.piece_type,
            'x': self.position.x,
            'y': self.position.y
        }