import pygame
from constraints import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #game loop
    while True:
        #background color
        screen.fill((0, 0, 0))

        #makes the window close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #screen refresh
        pygame.display.flip()


if __name__ == "__main__":
    main()
