from .debug_drawer import DebugDrawer
from .wall import Wall
from .token import Token

class World(object):
    def __init__(self, width=10, height=10, pieces=None, walls=None, drawer=None):
        self.width = width
        self.height = height
        self.pieces = {} if pieces is None else pieces
        self.walls = [] if walls is None else walls
        self.drawer = DebugDrawer() if drawer is None else drawer
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

    def is_token(self, position):
        return self.get_token(position) is not None

    def get_token(self, position):
        for piece in self.pieces:
            if isinstance(piece, Token) and piece.position == position:
                return piece
        return None

    def on_move(self, piece_id, after_position):
        self.drawer.on_move(piece_id, after_position)

    def on_rotate(self, piece_id, after_direction):
        self.drawer.on_rotate(piece_id, after_direction)