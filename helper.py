from .urobot.direction import Direction
from .urobot.drawer import Drawer
from .urobot.piece import Piece
from .urobot.position import Position
from .urobot.robot import Robot as GeneralRobot
from .urobot.wall import Wall
from .urobot.world import World, load_world_from_save
import json

def create_world(**kwargs):
    global __urobots__
    __urobots__ = {}
    __urobots__['world'] = World(**kwargs)

def load_world(file_path, drawer=None):
    global __urobots__
    with open(file_path, 'r') as world_file:
        world_save = json.loads(world_file.read())
    __urobots__ = {}
    __urobots__['world'] = load_world_from_save(world_save)

class Robot(GeneralRobot):
    def __init__(self, **kwargs):
        global __urobots__
        super().__init__(**kwargs)
        __urobots__['world'].add_piece(self)

__all__ = [
    'create_world',
    'load_world',
    'Robot'
]