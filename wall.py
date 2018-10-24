class Wall(object):
    def __init__(self, position_1, position_2):
        self.position_1 = position_1
        self.position_2 = position_2

    def __eq__(self, other):
        self_positions = [self.position_1.to_list(), self.position_2.to_list()]
        other_positions = [other.position_1.to_list(), other.position_2.to_list()]
        self_positions.sort()
        other_positions.sort()
        return self_positions == other_positions

    def __ne__(self, other):
        return not self == other

    def to_dict(self):
        return {
            'x1': self.position_1.x,
            'y1': self.position_1.y,
            'x2': self.position_2.x,
            'y2': self.position_2.y
        }