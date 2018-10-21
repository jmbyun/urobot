from .piece import Piece
from .direction import Direction
from .position import Position

class RobotException(Exception):
    pass

class Robot(Piece):
    def __init__(self, position=None, direction=None, beepers=0):
        super().__init__(position, direction)
        self.piece_type = 'robot'
        self.beepers = []
        for _ in range(beepers):
            self.beepers.append(Beeper())

    def move(self):
        after_position = self.position + self.direction.get_delta()
        if not self.world.is_in_world(after_position):
            raise RobotException('Cannot move! I cannot go out of the world!')
        if self.world.is_wall_between(self.position, after_position):
            raise RobotException('Cannot move! There is a wall in front of me!')
        self.position = after_position
        if self.world:
            self.world.on_move(self.id, self.position)

    def turn_left(self):
        self.direction = self.direction.get_next()
        if self.world:
            self.world.on_rotate(self.id, self.direction)

    def is_adjacent_position_clear(self, position):
        is_front_in_world = self.world.is_in_world(position)
        is_no_wall_front = not self.world.is_wall_between(self.position, position)
        return is_front_in_world and is_no_wall_front

    def is_front_clear(self):
        return self.is_adjacent_position_clear(self.position + self.direction.get_delta())

    def is_left_clear(self):
        return self.is_adjacent_position_clear(self.position + self.direction.get_next().get_delta())

    def is_right_clear(self):
        return self.is_adjacent_position_clear(self.position + self.direction.get_prev().get_delta())

    def is_facing_up(self):
        return self.direction == Direction('up')

    def has_beepers(self):
        return bool(self.beepers)

    def is_on_beepers(self):
        return self.world.is_beeper(self.position)

    def pick_beeper(self):
        beeper = self.world.get_beeper(self.position)
        if beeper is None:
            raise RobotException('There is no beeper to pick up!')
        self.world.remove_piece(self, beeper.id)
        self.beepers.append(beeper)

    def drop_beeper(self):
        if not self.beepers:
            raise RobotException('I have no beepers to drop!')
        beeper = self.beepers.pop()
        beeper.set_position(self.position.clone())
        self.world.add_piece(beeper)