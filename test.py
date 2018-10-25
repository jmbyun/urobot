import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from urobot.helper import *
from urobot import Wall, Position

def turn_right():
    for i in range(3):
        robot.turn_left()

create_world(walls=[Wall(Position(1, 0), Position(2, 0))])
robot = Robot(beepers=1)
robot.set_pause(0.2)
robot.set_trace('blue')
robot.move()
robot.drop_beeper()
robot.turn_left()
robot.move()
turn_right()
robot.move()
turn_right()
robot.move()
robot.turn_left()

for i in range(10):
    robot.move()