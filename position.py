class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def clone(self):
        return Position(self.x, self.y)

    def to_list(self):
        return [self.x, self.y]