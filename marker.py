from .piece import Piece

class Marker(Piece):
    def __init__(self, position=None):
        super().__init__(position=position)
        self.piece_type = 'marker'
        self.marker_type = 'marker'

    def to_dict(self): 
        return {
            **(super().to_dict()),
            'marker_type': self.marker_type
        }

    def set_position(self, position):
        self.position = position
        if self.world:
            self.world.on_move(self)