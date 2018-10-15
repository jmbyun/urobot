from drawer import Drawer

class DebugDrawer(Drawer):
    def __init__(self):
        pass

    def draw(self, width, height, pieces, walls):
        print('DebugDrawer: Draw a world of %dx%d.' % (width, height))
        for p in pieces.values():
            print('DebugDrawer: Draw piece of type "%s" on (%d, %d) heading %r with ID %s.' % (
                p.piece_type, p.position.x, p.position.y, p.direction, p.id))
        for w in walls:
            print('DebugDrawer: Draw wall between (%d, %d) and (%d, %d).' % (
                w.position_1.x, w.position_1.y, w.position_2.x, w.position_2.y))

    def on_add_piece(self, piece):
        print('DebugDrawer: Add piece of type "%s" on (%d, %d) heading %r with ID %s.' % (
                piece.piece_type, piece.position.x, piece.position.y, piece.direction, piece.id))

    def on_remove_piece(self, piece_id):
        print('DebugDrawer: Remove piece with ID %s.' % piece_id)

    def on_move(self, piece_id, after_position):
        print('DebugDrawer: Move piece with id %s to (%d, %d).' % (
            piece_id, after_position.x, after_position.y))

    def on_rotate(self, piece_id, after_direction):
        print('DebugDrawer: Rotate piece with id %s to %r.' % (
            piece_id, after_direction))