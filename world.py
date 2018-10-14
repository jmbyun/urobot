from debug_drawer import DebugDrawer
from wall import Wall

class World(object):
    def __init__(self, width=10, height=10, pieces={}, walls=[], drawer=None):
        self.width = width
        self.height = height
        self.pieces = pieces
        self.walls = walls
        if drawer is None:
            self.drawer = DebugDrawer()
        else:
            self.drawer = drawer
        self.drawer.set_world(self)
        self.drawer.draw(width, height, pieces, walls)

    def add_piece(self, piece):
        piece.id = len(self.pieces)
        piece.world = self
        self.pieces[piece.id] = piece
        self.drawer.on_add_piece(piece)

    def remove_piece(self, piece_id):
        piece = self.pieces[piece_id]
        piece.id = None
        piece.world = None
        del self.pieces[piece_id]
        self.drawer.on_remove_piece(piece_id)

    def is_in_world(self, position):
        return 0 <= position.x < self.width and 0 <= position.y < self.height

    def is_wall_between(self, position_1, position_2):
        wall = Wall(position_1, position_2)
        return wall in self.walls

    def on_move(self, piece_id, after_position):
        self.drawer.on_move(piece_id, after_position)

    def on_rotate(self, piece_id, after_direction):
        self.drawer.on_rotate(piece_id, after_direction)