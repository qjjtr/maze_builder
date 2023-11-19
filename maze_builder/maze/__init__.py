from maze.maze import *
from maze.generators import *
from maze.maze_visitor import *
from maze.runners import *

def create_maze(size, generator):
    if not generator in GENERATORS:
        return None

    return Maze(GENERATORS[generator], size[0], size[1])

def get_generators():
    return list(GENERATORS.keys())
