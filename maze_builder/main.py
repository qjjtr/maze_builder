import pygame

pygame.init()

from maze.generators import *
from maze.maze_visitor import *
from maze.runners import *
from ui.screens import *

sc = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Maze builder")
sc.fill(THECOLORS['yellow'])

menu(sc)
