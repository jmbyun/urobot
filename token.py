from .piece import Piece
from .direction import Direction
from .position import Position

class Token(Piece):
    def __init__(self, position=None):
        super().__init__(position)
        self.piece_type = 'Token'

    def set_position(self, position):
        self.position = position
        if self.world:
            self.world.on_move(self.id, self.position)