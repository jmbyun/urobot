from .web_drawer import WebDrawer
from .wall import Wall, load_wall_from_save
from .beeper import Beeper
from .piece import load_piece_from_save

def load_world_from_save(world_save, drawer=None):
    return World(
        width=world_save['width'],
        height=world_save['height'],
        pieces={k: load_piece_from_save(p) for k, p in world_save['pieces'].items()},
        walls=[load_wall_from_save(w) for w in world_save['walls']],
        drawer=drawer
    )

class World(object):
    def __init__(self, width=10, height=10, pieces=None, walls=None, drawer=None):
        self.width = width
        self.height = height
        self.pieces = {} if pieces is None else pieces
        self.walls = [] if walls is None else walls
        self.drawer = WebDrawer() if drawer is None else drawer
        self.drawer.set_world(self)
        self.drawer.draw(width, height, self.pieces, self.walls)

    def to_save(self):
        return {
            'type': 'world',
            'width': self.width,
            'height': self.height,
            'pieces': {k: p.to_save() for k, p in self.pieces.items()},
            'walls': [w.to_save() for w in self.walls]
        }

    def add_piece(self, piece):
        piece.id = len(self.pieces)
        piece.world = self
        self.pieces[piece.id] = piece
        self.drawer.on_add(piece)

    def remove_piece(self, piece_id):
        piece = self.pieces[piece_id]
        piece.id = None
        piece.world = None
        del self.pieces[piece_id]
        self.drawer.on_remove(piece_id)

    def is_in_world(self, position):
        return 0 <= position.x < self.width and 0 <= position.y < self.height

    def is_wall_between(self, position_1, position_2):
        wall = Wall(position_1, position_2)
        return wall in self.walls

    def is_beeper(self, position):
        return self.get_beeper(position) is not None

    def get_beeper(self, position):
        for piece in self.pieces:
            if isinstance(piece, Beeper) and piece.position == position:
                return piece
        return None

    def on_move(self, piece):
        self.drawer.on_move(piece)

    def on_rotate(self, piece):
        self.drawer.on_rotate(piece)