import sys
import pygame
from pygame.locals import *

COLORS = [
    (0, 0, 0),  # BLACK
    (0, 0, 255),  # BLUE
    (0, 255, 0),  # GREEN
    (0, 255, 255),  # CYAN
    (255, 0, 0),  # RED
    (255, 0, 255),  # MAGENTA
    (255, 255, 0),  # YELLOW
    (255, 255, 255)  # WHITE
]

if __name__ == "__main__":
    pygame.init()

    changed = True
    index, last_index = 0, 0
    screen = pygame.display.set_mode((640, 360), RESIZABLE)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    index = (index - 1) % len(COLORS)
                elif event.key == K_RIGHT:
                    index = (index + 1) % len(COLORS)

        if index != last_index:
            changed = True

        if changed:
            screen.fill(COLORS[index])
            pygame.display.update()
