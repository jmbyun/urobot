# from .world import World 
# from .wall import Wall
# from .position import Position
# from .robot import Robot

# def turn_right():
#     for i in range(3):
#         robot.turn_left()

# world = World(walls=[Wall(Position(1, 0), Position(2, 0))])
# robot = Robot()
# world.add_piece(robot)
# robot.move()
# robot.turn_left()
# robot.move()
# turn_right()
# robot.move()
# turn_right()
# robot.move()
# robot.turn_left()
# for i in range(10):
#     robot.move()

import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from urobots.helper import *

def turn_right():
    for i in range(3):
        robot.turn_left()

create_world()
robot = Robot()
robot.move()
robot.turn_left()
robot.move()
turn_right()
robot.move()
turn_right()
robot.move()
robot.turn_left()
for i in range(10):
    robot.move()