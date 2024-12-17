import pygame
from constaints import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #makes a clock object for later limiting fps
    clock = pygame.time.Clock()
    dt = 0
    
    #instantiate a player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    #game loop
    while True:
        #background color
        screen.fill((0, 0, 0))

        #calculates delta
        dt = clock.tick() / 1000

        #render the player
        player.draw(screen)

        #checks for player inputs and such
        player.update(dt)

        #makes the window close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #screen refresh
        pygame.display.flip()


if __name__ == "__main__":
    main()
