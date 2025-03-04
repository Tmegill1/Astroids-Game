import pygame
from constants import *
from player import *


def main():
    print("Starting Astroids")
    print("Screen Width " , SCREEN_WIDTH)
    print("Screen Height " , SCREEN_HEIGHT)
    pygame.init()
    clock  = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        screen.fill((0,0,0)) #setting color of box
        player.draw(screen)
        player.update(dt)


        #framerate and exiting game
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        clock.tick(60)
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()