from enum import Enum

class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)


START_POSITION = (0, 1)

def printer(item):
    if item[0]:
        print(item[0])
    if item[1]:
        print(item[1])
    print()
