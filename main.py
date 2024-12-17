import pygame
from constraints import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #makes a clock object for later limiting fps
    clock = pygame.time.Clock()
    dt = 0

    #game loop
    while True:
        #background color
        screen.fill((0, 0, 0))

        #calculates delta
        dt = clock.tick() / 1000

        #makes the window close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #screen refresh
        pygame.display.flip()


if __name__ == "__main__":
    main()
