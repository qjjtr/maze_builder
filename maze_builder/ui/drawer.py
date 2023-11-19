from ui.constants import *

import pygame

def clear_up(sc):
    pygame.draw.rect(sc, BACKGROUND_COLOR, pygame.Rect(0, 0, WIDTH, BACKGROUND_HEIGHT), 0)

def clear_text(sc):
    pygame.draw.rect(sc, TEXT_BACKGROUND_COLOR, pygame.Rect(0, BACKGROUND_HEIGHT, WIDTH, TEXT_FIELD_HEIGHT), 0)

def draw_maze(sc, maze, solution=None):
    clear_up(sc)
    if maze == None:
        return
    maze = maze.split('\n')
    n, m = len(maze), len(maze[0])
    if WIDTH // m < BACKGROUND_HEIGHT // n:
        length = WIDTH // m
        start_coordinates = (0, (BACKGROUND_HEIGHT - n * length) // 2)
    else:
        length = BACKGROUND_HEIGHT // n
        start_coordinates = ((WIDTH - m * length) // 2, 0)
    for i in range(n):
        for j in range(m):
            sym = maze[i][j]
            coord = (start_coordinates[0] + j * length, start_coordinates[1] + i * length)
            if sym == '#':
                pygame.draw.rect(sc, WALL_COLOR, pygame.Rect(coord, (length, length)), 0)
            elif sym == '@':
                pygame.draw.circle(sc, RUNNER_COLOR, (coord[0] + length // 2, coord[1] + length // 2), length * 2 // 5, 0)
            else:
                True
    if solution == None:
        return

    path = list(map(lambda coord : (length // 2 + start_coordinates[0] + coord[1] * length, length // 2 + start_coordinates[1] + coord[0] * length), solution))
    pygame.draw.lines(sc, SOLUTION_COLOR, False, path, length // 3)

def draw_text(sc, text):
    clear_text(sc)
    if text != None:
        text = FONT.render(text, True, TEXT_COLOR)
        sc.blit(text, TEXT_COORDINATES)


def draw_options(sc, header, options):
    clear_up(sc)
    n = len(options) + 1
    text_coordinates = (WIDTH // 6 + 20, (BACKGROUND_HEIGHT - n * (OPTIONS_TEXT_SIZE + 40)) // 2 + 20)
    rect_coordinates = (text_coordinates[0] - 20, text_coordinates[1] - 20)
    rect_size = (WIDTH * 2 // 3, n * (OPTIONS_TEXT_SIZE + 40))
    pygame.draw.rect(sc, OPTIONS_TEXT_BACKGROUND_COLOR, pygame.Rect(rect_coordinates, rect_size), 0)
    lines = [header]
    lines.extend(options)
    for text in lines:
        text = OPTIONS_FONT.render(text, True, OPTIONS_TEXT_COLOR)
        sc.blit(text, text_coordinates)
        text_coordinates = (text_coordinates[0], text_coordinates[1] + 40 + OPTIONS_TEXT_SIZE)
