from .position import Position

class Direction(object):
    def __init__(self, direction):
        self.direction = direction.lower()[0]
        if self.direction not in 'lrud':
            raise Exception('Unknown direction')

    def __str__(self):
        direction_dict = {
            'l': 'Left',
            'r': 'Right',
            'u': 'Up',
            'd': 'Down'
        }
        return direction_dict[self.direction]

    def __eq__(self, other):
        return self.direction == other.direction
    
    def __ne__(self, other):
        return not self == other

    def to_char(self):
        return self.direction

    def get_delta(self):
        if self.direction == 'l':
            return Position(-1, 0)
        elif self.direction == 'r':
            return Position(1, 0)
        elif self.direction == 'u':
            return Position(0, 1)
        elif self.direction == 'd':
            return Position(0, -1)

    def get_next(self):
        directions = 'ldru'
        return Direction(directions[(directions.index(self.direction) + 1) % 4])

    def get_prev(self):
        directions = 'ldru'
        return Direction(directions[(directions.index(self.direction) - 1) % 4])
            