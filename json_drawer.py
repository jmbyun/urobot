from .drawer import Drawer
import json

class JsonDrawer(Drawer):
    def __init__(self):
        super().__init__()

    def print(self, s):
        print(s)

    def print_dict(self, out_dict):
        self.print(json.dumps(out_dict))
    
    def draw(self, width, height, pieces, walls):
        self.print_dict({
            'task': 'draw_world',
            'width': width,
            'height': height
        })
        for p in pieces.values():
            self.print_dict({
                'task': 'draw_piece',
                'piece_type': p.piece_type,
                'piece_id': p.id,
                'x': p.position.x,
                'y': p.position.y,
                'direction': p.direction.direction
            })
        for w in walls:
            self.print_dict({
                'task': 'draw_wall',
                'x1': w.position_1.x,
                'y1': w.position_1.y,
                'x2': w.position_2.x,
                'y2': w.position_2.y
            })

    def on_add(self, piece):
        self.print_dict({
            'task': 'draw_piece',
            'piece_type': piece.piece_type,
            'piece_id': piece.id,
            'x': piece.position.x,
            'y': piece.position.y,
            'direction': piece.direction.direction
        })

    def on_remove(self, piece_id):
        self.print_dict({
            'task': 'remove_piece',
            'piece_id': piece_id
        })

    def on_move(self, piece_id, after_position):
        self.print_dict({
            'task': 'move_piece',
            'piece_id': piece_id,
            'x': after_position.x,
            'y': after_position.y
        })

    def on_rotate(self, piece_id, after_direction):
        self.print_dict({
            'task': 'rotate_piece',
            'piece_id': piece_id,
            'direction': after_direction.direction
        })