from ui.drawer import *

import pygame
import sys

def key_yielder():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                yield event


def get_key():
    return next(key_yielder())

def get_option():
    while True:
        key = get_key().key
        if key > 0 and key < 128:
            return chr(key)

def wrong_option(sc):
    draw_text(sc, "wrong option")
    pygame.display.flip()
