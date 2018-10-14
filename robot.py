from piece import Piece

class MoveException(Exception):
    pass

class Robot(Piece):
    def __init__(self, position=None, direction=None):
        super().__init__(position, direction)
        self.piece_type = 'Robot'

    def move(self):
        after_position = self.position + self.direction.get_delta()
        if not self.world.is_in_world(after_position):
            raise MoveException('Cannot move! I cannot go out of the world!')
        if self.world.is_wall_between(self.position, after_position):
            raise MoveException('Cannot move! There is a wall in front of me!')
        self.position = after_position
        self.world.on_move(self.id, self.position)

    def turn_left(self):
        self.direction = self.direction.get_next()
        self.world.on_rotate(self.id, self.direction)

    def is_front_clear(self):
        after_position = self.position + self.direction.get_delta()
        self.world.is_in_world(after_position)
        return self.world.is_in_world(after_position) and not self.world.is_wall_between(self.position, after_position)

    def front_is_clear(self):
        return self.is_front_clear()
