import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    print("Starting Astroids")
    print("Screen Width " , SCREEN_WIDTH)
    print("Screen Height " , SCREEN_HEIGHT)
    pygame.init()
    clock  = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Sprites for updating
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidField = pygame.sprite.Group()

    #container
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)


    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        screen.fill((0,0,0)) #setting color of box
        #player.draw(screen)
        #player.update(dt)
        updatable.update(dt)
        for sprite in drawable:   #Goes throuugh all player group in drawable
            sprite.draw(screen)

# After the update step
        for asteroid in asteroids:  # Iterate through the asteroids group
            if player.collision(asteroid):  # Check collision between player and asteroid
              print("Game Over!")
              sys.exit()  # Exit the program
                



        #framerate and exiting game
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        clock.tick(60)
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()