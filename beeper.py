from .marker import Marker
from .direction import Direction
from .position import Position

class Beeper(Marker):
    def __init__(self, position=None):
        super().__init__(position)
        self.marker_type = 'beeper'