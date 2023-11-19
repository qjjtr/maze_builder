from ui.base import *
from ui.drawer import *
from ui.constants import *
from maze import *

import pygame
import sys

def menu(sc):
    draw_options(sc, 'MAZE BUILDER', ['1. new maze', 'esc. exit'])
    pygame.display.flip()
    while True:
        option = get_option()
        if option == '1':
            new_maze(sc)
            return
        elif option == chr(pygame.K_ESCAPE):
            sys.exit()
        else:
            wrong_option(sc)

def new_maze(sc):
    draw_options(sc, 'CHOOSE MAZE', ['1. small', '2. medium', '3. big', '4. extended options', 'esc. exit'])
    pygame.display.flip()

    while True:
        option = get_option()
        if option == '1':
            maze = create_maze(SMALL, DEFAULT_GENERATOR)
            run_maze(sc, maze)
            return
        elif option == '2':
            maze = create_maze(MEDIUM, DEFAULT_GENERATOR)
            run_maze(sc, maze)
            return
        elif option == '3':
            maze = create_maze(BIG, DEFAULT_GENERATOR)
            run_maze(sc, maze)
            return
        elif option == '4':
            extended_options(sc)
            return
        elif option == chr(pygame.K_ESCAPE):
            menu(sc)
            return
        else:
            wrong_option(sc)

def get_number(sc, header):
    number = 0
    while True:
        draw_options(sc, header, ['> ' + str(number)])
        pygame.display.flip()
        option = get_option()
        if option >= '0' and option <= '9':
            number = 10 * number + int(option)
        elif option == chr(pygame.K_ESCAPE):
            return None
        elif option == chr(pygame.K_BACKSPACE):
            number //= 10
        elif option == chr(pygame.K_RETURN):
            break
    return number

def extended_options(sc):
    m = get_number(sc, 'ENTER MAZE WIDTH')
    if m == None:
        menu(sc)
        return

    n = get_number(sc, 'ENTER MAZE HEIGHT')
    if n == None:
        menu(sc)
        return

    generators = get_generators()
    options = list(map(lambda x : str(x[0]) + '. ' + x[1], enumerate(generators, 1)))
    options.append('esc. exit')

    draw_options(sc, 'CHOOSE GENERATION TYPE', options)
    pygame.display.flip()

    while True:
        option = get_option()
        if option >= '0' and option <= '9':
            if int(option) <= len(generators):
                generator = generators[int(option) - 1]
                break
            else:
                wrong_option(sc)
        elif option == chr(pygame.K_ESCAPE):
            menu(sc)
            return
        else:
            wrong_option(sc)

    maze = create_maze((n, m), generator)
    run_maze(sc, maze)

def draw_listener(sc):
    def listener(item):
        draw_maze(sc, item[0])
        draw_text(sc, item[1])
        pygame.display.flip()

    return listener

def run_maze(sc, maze):
    visitor = MazeVisitor(maze)
    while True:
        visitor.run(user_runner(key_yielder), draw_listener(sc))
        if visitor.is_exit():
            menu(sc)
            return

        draw_options(sc, 'PAUSE', ['1. continue', '2. show solution', 'esc. exit'])
        pygame.display.flip()

        option = get_option()
        if option == '1':
            continue
        if option == '2':
            show_solution(sc, maze)
            return
        elif option == chr(pygame.K_ESCAPE):
            menu(sc)
            return
        else:
            wrong_option(sc)

def show_solution(sc, maze):
    draw_maze(sc, maze.__str__(), get_solution(maze))
    pygame.display.flip()

    get_key()
    menu(sc)
