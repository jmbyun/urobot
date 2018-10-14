from position import Position
from direction import Direction

class Piece(object):
    def __init__(self, position=None, direction=None):
        if position is None:
            self.position = Position(0, 0)
        else:
            self.position = position
        if direction is None:
            self.direction = Direction('r')
        else:
            self.direction = direction
        self.id = None
        self.world = None
        self.piece_type = None