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

    index = 0
    update_screen = True
    screen = pygame.display.set_mode((640, 360), RESIZABLE)

    pygame.display.set_caption("PixelBuddy")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                last_index = index

                if event.key == K_LEFT:
                    index = (index - 1) % len(COLORS)
                elif event.key == K_RIGHT:
                    index = (index + 1) % len(COLORS)

                if index != last_index:
                    update_screen = True  # update the color
            elif event.type == VIDEORESIZE or event.type == VIDEOEXPOSE:
                update_screen = True  # updates the screen when resized or minimized/maximized

        if update_screen:
            screen.fill(COLORS[index])
            pygame.display.update()
            update_screen = False
